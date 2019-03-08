import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="compare-equal",
    version="0.1",
    description="Third-party chimera module for compare molecules",
    long_description = long_description
    author="Andres Giner Anton",
    author_email="andresgineranton@outlook.com",
    py_modules=["compare.py"],
    url="https://github.com/andresginera/compare-equal",
)

