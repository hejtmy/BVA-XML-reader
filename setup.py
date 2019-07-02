import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="bvareader",
    version="0.1.3",
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
    tests_require=["pytest", ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
    entry_points={
      'console_scripts': [
        'bva-preprocess-xml = bvareader.commands:sys_bva_preprocess_xml',
        'bva-positions-table = bvareader.commands:bva_positions_table',
        'bva-phases-table = bvareader.commands:bva_phases_table',
        'bva-measures-start-stop-table = bvareader.commands:bva_measure_start_stop_table',
        'bva-sync-times-table = bvareader.commands:bva_sync_times_table',
        'bva-settings-to-csv = bvareader.commands:xml_settings_to_csv',
        ]
    }
)