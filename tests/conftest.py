import pytest


@pytest.fixture
def bva_xml_data_path():
    return "tests/test_data/example_bva.xml"


@pytest.fixture
def sync_csv_data_path():
    return "tests/test_data/example_sync.csv"


@pytest.fixture
def settings_xml_data_path():
    return 'tests/test_data/example_test_settings.xml'
