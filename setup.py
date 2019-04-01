import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bva-reader",
    version="0.0.1",
    author="Lukáš Hejtmy Hejtmánek",
    author_email="hejtmy@gmail.com",
    description="Package to read and process BVA data from LF Motol",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)