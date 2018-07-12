import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygolos",
    version="0.0.1",
    author="Test",
    author_email="serebreanu.v@gmail.com",
    description="GOLOS PYApi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kozakovi4/pygolos/",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)