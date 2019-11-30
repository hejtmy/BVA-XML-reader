import bvareader.new_bva.preprocessing as new_preprocessing


def preprocess_bva_data(pd_bva):
    pd_bva_prep = new_preprocessing.preprocess_bva_data(pd_bva)
    return(pd_bva_prep)


def add_rotation(pd_bva):
    pd_bva_prep = new_preprocessing.add_rotation(pd_bva)
    return(pd_bva_prep)
