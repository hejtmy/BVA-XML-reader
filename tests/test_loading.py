import pytest
from bvareader import reader
import pandas as pd


@pytest.fixture
def bva_xml_data_path():
    return "tests/test_data/example_bva.xml"


@pytest.fixture
def bva_xml_data_path():
    return "tests/test_data/example_sync.xml"


def test_loading_bva_xml(bva_xml_data_path):
    pd_bva = reader.read_xml_bva(bva_xml_data_path)
    assert isinstance(pd_bva, pd.core.frame.DataFrame)


def test_loading_sync_csv():
    reader.read_sync_file("example_data/example.csv")