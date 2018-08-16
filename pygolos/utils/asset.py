import re
import struct
from varint import encode


class Asset:

    def __init__(self, string: str):
        assert re.fullmatch(r"^[0-9]+\.?[0-9]* [A-Za-z0-9]+$", string),\
            "Expecting amount like '99.000 SYMBOL', instead got '" + string + "'"
        self.__amount, self.__symbol = string.split(" ")
        if len(self.__symbol) > 6:
            raise Exception("Symbols are not longer than 6 characters " + self.__symbol + "-" + len(self.__symbol))

    @property
    def amount(self):
        return self.__amount

    @property
    def symbol(self):
        return self.__symbol

    def __bytes__(self):
        buffer = b""
        buffer += struct.pack("q", int(self.__amount.replace(".", "")))
        dot = self.__amount.index(".")
        precision = 0 if dot == -1 else len(self.__amount) - dot - 1
        buffer += bytes([precision])
        buffer += bytes(self.__symbol.upper(), "ascii")
        for i in range(7 - len(self.__symbol)):
            buffer += b"\x00"
        return buffer

    def __str__(self):
        if self["asset"] == "GDB":
            prec = 3
        elif self["asset"] == "GOLOS":
            prec = 3
        elif self["asset"] == "GESTS":
            prec = 6
        else:
            prec = 6
        return "{:.{prec}f} {}".format(
            self.__amount, self.__symbol, prec=prec)
