import pandas as pd


def read_sync_file(path):
    pd_sync = pd.read_csv(path, sep=",")
    pd_sync.time = (pd.to_datetime(pd_sync.time, format='%H:%M:%S') - pd.to_datetime("00:00:00", format='%H:%M:%S')).dt.total_seconds()
    pd_sync.time = pd_sync.time + pd_sync.ms / 1000
    return(pd_sync)