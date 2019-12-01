from bvareader import reader as reader
from bvareader.new_bva import reader as new_reader
from bvareader.old_bva import reader as old_reader
import pandas as pd


# TESTING NEW BVA
def test_loading_new_bva_position(bva_xml_data_path):
    pd_bva = new_reader.read_xml_bva(bva_xml_data_path)
    assert isinstance(pd_bva, pd.core.frame.DataFrame)
    pd_bva2 = reader.read_positions(bva_xml_data_path)
    assert pd_bva.equals(pd_bva2)


def test_loading_new_bva_sync(bva_xml_data_path):
    pd_bva = new_reader.read_xml_sync(bva_xml_data_path)
    assert isinstance(pd_bva, pd.core.frame.DataFrame)
    pd_bva2 = reader.read_sync_times(bva_xml_data_path)
    assert pd_bva.equals(pd_bva2)


def test_loading_new_bva_phases(bva_xml_data_path):
    pd_bva = new_reader.read_xml_phases(bva_xml_data_path)
    assert isinstance(pd_bva, pd.core.frame.DataFrame)
    pd_bva2 = reader.read_phases(bva_xml_data_path)
    assert pd_bva.equals(pd_bva2)


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
def test_loading_old_position(bva_old_data_path):
    position = old_reader.read_position(bva_old_data_path)
    assert isinstance(position, pd.core.frame.DataFrame)


def test_loading_old_phases(bva_old_data_path):
    phases = old_reader.read_phases(bva_old_data_path)
    assert isinstance(phases, pd.core.frame.DataFrame)


def test_loading_old_settings(bva_old_data_path):
    settings = old_reader.read_settings(bva_old_data_path)
    assert isinstance(settings, pd.core.frame.DataFrame)
