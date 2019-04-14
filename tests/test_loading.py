import pytest
from bvareader import reader
import pandas as pd


@pytest.fixture
def bva_xml_data_path():
    return "tests/test_data/example_bva.xml"


@pytest.fixture
def sync_csv_data_path():
    return "tests/test_data/example_sync.csv"


def test_loading_bva_xml(bva_xml_data_path):
    pd_bva = reader.read_xml_bva(bva_xml_data_path)
    assert isinstance(pd_bva, pd.core.frame.DataFrame)


def test_loading_sync_csv(sync_csv_data_path):
    pd_sync = reader.read_sync_file(sync_csv_data_path)
    assert isinstance(pd_sync, pd.core.frame.DataFrame)
