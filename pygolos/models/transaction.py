import hashlib
import struct
from binascii import unhexlify, hexlify
import ecdsa
from pygolos.utils.base58 import Base58


import time
from calendar import timegm
from json import dumps
from pygolos.api import Api

import varint

_operations = {"vote": b"\0", "comment": b"\1", "collection": b"\x3c", "rate": b"\x3d"}

class Transaction:
    def __init__(self,
                 ref_block_num: int = int(),
                 ref_block_prefix: int = int(),
                 expiration: str=str(),
                 operations: list = list()):
        self.ref_block_num = ref_block_num
        self.ref_block_prefix = ref_block_prefix
        self.expiration = expiration
        self.operations = operations
        self.extensions = []
        self.signatures = []

    def binarify(self):
        buffer = b""
        buffer += struct.pack("<H", self.ref_block_num)
        buffer += struct.pack("<I", self.ref_block_prefix)
        buffer += struct.pack("<I", timegm(time.strptime((self.expiration + "UTC"), "%Y-%m-%dT%H:%M:%S%Z")))
        buffer += bytes(varint.encode(len(self.operations)))
        for op in self.operations:
            buffer += _operations[op.__class__.__name__.lower()]
            buffer += op.binarify()
            print(_operations[op.__class__.__name__.lower()])
        buffer += bytes(varint.encode(len(self.extensions)))
        return buffer


    def jsonify(self):
        obj = self.__dict__.copy()
        obj["operations"] = [[operation.__class__.__name__.lower(), operation.__dict__] for operation in self.operations]
        return dumps(obj)

    def sign(self, keys: list):
        message = unhexlify(Api.chain_id) + self.binarify()
        digest = hashlib.sha256(message).digest()

        for key in keys:
            _wif = key if isinstance(key, Base58) else Base58(key)
            p = bytes(_wif.__bytes__())
            sk = ecdsa.SigningKey.from_string(p, curve=ecdsa.SECP256k1)
            cnt = 0
            i = 0
            while 1:
                cnt += 1
                # Deterministic k
                #
                k = ecdsa.rfc6979.generate_k(
                    sk.curve.generator.order(),
                    sk.privkey.secret_multiplier,
                    hashlib.sha256,
                    hashlib.sha256(digest + bytes([cnt])).digest())
                # Sign message
                #
                sigder = sk.sign_digest(
                    digest,
                    sigencode=ecdsa.util.sigencode_der,
                    k=k)
                # Reformating of signature
                #
                r, s = ecdsa.util.sigdecode_der(sigder, sk.curve.generator.order())
                signature = ecdsa.util.sigencode_string(r, s, sk.curve.generator.order())

                # Make sure signature is canonical!
                #
                lenR = sigder[3]
                lenS = sigder[5 + lenR]
                if lenR is 32 and lenS is 32:
                    # Derive the recovery parameter
                    #
                    i = recoverPubkeyParameter(digest, signature, sk.get_verifying_key())
                    i += 4  # compressed
                    i += 27  # compact
                    break
            self.signatures.append(hexlify(struct.pack("<B", i) + signature).decode("ascii"))
            print(self.jsonify())


def recover_public_key(digest, signature, i):
    """ Recover the public key from the the signature
    """
    # See http : //www.secg.org/download/aid-780/sec1-v2.pdf section 4.1.6 primarily
    curve = ecdsa.SECP256k1.curve
    G = ecdsa.SECP256k1.generator
    order = ecdsa.SECP256k1.order
    yp = (i % 2)
    r, s = ecdsa.util.sigdecode_string(signature, order)
    # 1.1
    x = r + (i // 2) * order
    # 1.3. This actually calculates for either effectively 02||X or 03||X depending on 'k' instead of always for 02||X as specified.
    # This substitutes for the lack of reversing R later on. -R actually is defined to be just flipping the y-coordinate in the elliptic curve.
    alpha = ((x * x * x) + (curve.a() * x) + curve.b()) % curve.p()
    beta = ecdsa.numbertheory.square_root_mod_prime(alpha, curve.p())
    y = beta if (beta - yp) % 2 == 0 else curve.p() - beta
    # 1.4 Constructor of Point is supposed to check if nR is at infinity.
    R = ecdsa.ellipticcurve.Point(curve, x, y, order)
    # 1.5 Compute e
    e = ecdsa.util.string_to_number(digest)
    # 1.6 Compute Q = r^-1(sR - eG)
    Q = ecdsa.numbertheory.inverse_mod(r, order) * (s * R + (-e % order) * G)
    # Not strictly necessary, but let's verify the message for paranoia's sake.
    if not ecdsa.VerifyingKey.from_public_point(Q, curve=ecdsa.SECP256k1).verify_digest(signature, digest,
                                                                                     sigdecode=ecdsa.util.sigdecode_string):
        return None
    return ecdsa.VerifyingKey.from_public_point(Q, curve=ecdsa.SECP256k1)


def recoverPubkeyParameter(digest, signature, pubkey):
    """ Use to derive a number that allows to easily recover the
        public key from the signature
    """
    for i in range(0, 4):
        p = recover_public_key(digest, signature, i)
        if p.to_string() == pubkey.to_string():
            return i
    return None
