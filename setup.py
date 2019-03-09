import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="compare_equal",
    version="0.4.1",
    description="Third-party chimera module for compare molecules",
    long_description=long_description,
    author="Andres Giner Anton",
    author_email="andresgineranton@outlook.com",
    packages=setuptools.find_packages(),
    url="https://github.com/andresginera/compare-equal",
)

