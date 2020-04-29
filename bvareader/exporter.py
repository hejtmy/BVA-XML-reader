def save_csv(df, path, dec_points=4):
    """ wrapper around pandas to_csv with default values set

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame to be saved
    path : str
        where to save it. including file extension
    dec_points : int
        how many decimal points should hte floats be rounded to

    Returns
    -------
    None
        the function simply saves the given dataframe to passed path
    """
    f = '%.' + str(dec_points) + 'f'
    df.to_csv(path, sep=";", index=False, float_format=f)
