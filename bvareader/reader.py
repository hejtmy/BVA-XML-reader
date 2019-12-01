import bvareader.new_bva.reader as new_reader
# import bvareader.old_bva.reader as old_reader


def read_positions(folder):
    if old_or_new(folder) == 'old':
        return None
    if old_or_new(folder) == 'new':
        return None


def read_sync_times(folder):
    return None


def read_phases(folder):
    path = get_bva_file(folder)
    if old_or_new(folder) == 'new':
        pd_phases = new_reader.read_xml_phases(path)
    return pd_phases


def read_xml_phases(path):
    pd_phases = new_reader.read_xml_phases(path)
    return(pd_phases)


def read_xml_sync(path):
    pd_times = new_reader.read_xml_sync(path)
    return(pd_times)


def read_xml_bva(path):
    pd_bva = new_reader.read_xml_bva(path)
    return(pd_bva)


def read_measure_start_stop(path):
    pd_start_stops = new_reader.read_measure_start_stop(path)
    return pd_start_stops


def read_xml_settings(path):
    pd_settings = new_reader.read_xml_settings(path)
    return pd_settings


def read_sync_file(path):
    pd_sync = new_reader.read_sync_file(path)
    return(pd_sync)


# ' Wrapper around
def save_csv(df, path, dec_points=4):
    f = '%.'+str(dec_points)+'f'
    df.to_csv(path, sep=";", index=False, float_format=f)


# '
def old_or_new(folder):
    """ returns 'old' or returns 'new' based on the folder contents' """
    return None


def get_bva_file(folder):
    return None
