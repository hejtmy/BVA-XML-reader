from bvareader import reader as new_reader
from bvareader.old_bva import reader as old_reader
import pandas as pd


# TESTING NEW BVA
def test_loading_bva_xml(bva_xml_data_path):
    pd_bva = new_reader.read_xml_bva(bva_xml_data_path)
    assert isinstance(pd_bva, pd.core.frame.DataFrame)


def test_loading_sync_csv(sync_csv_data_path):
    pd_sync = new_reader.read_sync_file(sync_csv_data_path)
    assert isinstance(pd_sync, pd.core.frame.DataFrame)


def test_loading_settings_xml(settings_xml_data_path):
    pd_settings = new_reader.read_xml_settings(settings_xml_data_path)
    assert isinstance(pd_settings, pd.core.frame.DataFrame)


def test_loading_measure_start(settings_xml_data_path):
    pd_start_stop = new_reader.read_measure_start_stop(settings_xml_data_path)
    assert isinstance(pd_start_stop, pd.core.frame.DataFrame)


# TESTING OLD BVA
def test_loading_tr3(bva_tr3_data_path):
    blocks = old_reader.read_tr(bva_tr3_data_path)
    assert len(blocks) == 3
    assert isinstance(blocks[2], pd.core.frame.DataFrame)
