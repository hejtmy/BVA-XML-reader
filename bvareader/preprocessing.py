import bvareader.new_bva.preprocessing as new_preprocessing
import bvareader.old_bva.preprocessing as old_preprocessing


def prepare_position(pd_bva):
    """Prepares the positional data to a uniform dataframe

    This function clears redundant columns, add important columns

    It works for both old nad new bva data, trying to create a uniform output 

    Parameters:
    ----------
    pd_bva : pandas.DataFrame
        loaded dataframe with bvareader.reader.read_positions function

    Returns
    --------
    pd_bva: pandas.DataFrame
        dataframe with standardized columns, with header, separated by semicolumn
        timestamp; position_x; position_y; rotation_x
    """
    if old_or_new(pd_bva) == 'new':
        pd_bva_prep = new_preprocessing.preprocess_bva_data(pd_bva)
    if old_or_new(pd_bva) == 'old':
        pd_bva_prep = old_preprocessing.preprocess_position(pd_bva) 
    return(pd_bva_prep)


def old_or_new(pd_bva):
    if 'Point_x' in pd_bva.columns:
        return 'new'
    if 'arenax' in pd_bva.columns:
        return 'old'
    return None
