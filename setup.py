import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="bvareader",
    version="0.1",
    author="Lukáš Hejtmy Hejtmánek",
    author_email="hejtmy@gmail.com",
    description="Package to read and process BVA data from LF Motol",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hejtmy/bva-reader",
    packages=setuptools.find_packages(),
    install_requires=[
      'pandas',
      'numpy>=1.16.0',
      'matplotlib',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
    entry_points={
      'console_scripts': [
        'bva-preprocess-xml = bvareader.commands:bva_preprocess_xml',
        'bva-settings-to-csv = bvareader.commands:xml_settings_to_csv',
        ]
    }
)