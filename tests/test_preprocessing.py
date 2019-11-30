from bvareader import preprocessing
from bvareader import reader
import pandas as pd


# NEW BVA PREPROCESSING
def test_preprocessing_new_bva(bva_xml_data_path):
    pd_bva = reader.read_xml_bva(bva_xml_data_path)
    pd_bva = preprocessing.preprocess_bva_data(pd_bva)
    assert isinstance(pd_bva, pd.core.frame.DataFrame)
