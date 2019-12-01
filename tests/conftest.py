import pytest
import os


@pytest.fixture
def bva_xml_data_path():
    return os.path.join('tests', 'test_data', 'new_bva', 'example_bva.xml')


@pytest.fixture
def sync_csv_data_path():
    return os.path.join('tests', 'test_data', 'new_bva', 'example_sync.csv')


@pytest.fixture
def settings_xml_data_path():
    return os.path.join('tests', 'test_data', 'new_bva', 'example_test_settings.xml')


@pytest.fixture
def bva_old_data_path():
    return os.path.join('tests', 'test_data', 'old_bva', 'test.TR3')
