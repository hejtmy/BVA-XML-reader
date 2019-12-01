import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="bvareader",
    version="0.3.0",
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
      'Click>=7.0',
      ],
    tests_require=["pytest", ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
    entry_points={
      'console_scripts': [
        'process-bva = bvareader.commands:process_bva_data',
        'bva-positions = bvareader.commands:process_bva_positions',
        'bva-phases = bvareader.commands:process_bva_phases',
        'bva-measures-start-stop = bvareader.commands:process_bva_measure_start_stop',
        'bva-sync-times = bvareader.commands:process_bva_sync_times',
        'xml-settings-to-csv = bvareader.commands:xml_settings_to_csv',
        ]
    }
)
