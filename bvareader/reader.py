import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime
from bvareader.helpers import flatten_list


def read_xml_phases(path):
    root = ET.parse(path).getroot()
    phase_times = []
    for phase in root.iter('Phase'):
        row = []
        # phase_time = 0
        tps = phase.findall("./MousePath/TimestampPoint")
        if len(tps) == 0:
            row = [float('nan'), float('nan'), float('nan')]
        else:
            row.append(real_timestamp(tps[0]))
            row.append(real_timestamp(tps[-1]))
            row.append(float(tps[-1].find('Timestamp').text))
        phase_times.append(row)
    pd_phases = pd.DataFrame(phase_times, columns=["timestamp_start", 
                             "timestamp_end", "claimed_length"])
    return(pd_phases)


def read_xml_sync(path):
    root = ET.parse(path).getroot()
    times = []
    for phase in root.iter('Phase'):
        for sync in phase.iter('SyncEEGAction'):
            times.append(real_timestamp(sync))
    return(times)


def read_xml_bva(path):
    root = ET.parse(path).getroot()
    POINTS = ['Point', 'Front', 'Left', 'Right']
    bva_mat = []
    continuous_time = 0
    for phase in root.iter('Phase'):
        for TimestampPoint in phase.iter('TimestampPoint'):
            # old points had only Timestamp
            phase_time = float(TimestampPoint.find('Timestamp').text)
            phase_datetime_real = real_timestamp(TimestampPoint)
            row = []
            row.append(phase_time + continuous_time)
            row.append(phase_datetime_real)
            for point in POINTS:
                xy = TimestampPoint.find(point)
                if xy is not None:
                    row.append(float(xy.find('X').text))
                    row.append(float(xy.find('Y').text))
                else:
                    row.append(float("NaN"))
                    row.append(float("NaN"))
            bva_mat.append(row)
        continuous_time += phase_time
    colnames = ['timestamp_bva', 'timestamp'] + (flatten_list([[x + "_x", x + "_y"] for x in POINTS])) #adds colnames for all the points
    pd_bva = pd.DataFrame(bva_mat, columns=colnames)
    return(pd_bva)


def real_timestamp(element):
    # timestamp real is in form of 01/29/2019 10:02:45.574
    dt = datetime.strptime(element.find('TimestampReal').text, 
                           '%m/%d/%Y %H:%M:%S.%f')
    return(float(dt.timestamp()))


def save_csv(pd_bva, path, dec_points=4):
    f = '%.'+str(dec_points)+'f'
    pd_bva.to_csv(path, sep=";", index=False, float_format=f)


def read_sync_file(path):
    pd_sync = pd.read_csv(path, sep=",")
    pd_sync.time = (pd.to_datetime(pd_sync.time, format='%H:%M:%S') - pd.to_datetime("00:00:00", format='%H:%M:%S')).dt.total_seconds()
    pd_sync.time = pd_sync.time + pd_sync.ms / 1000
    return(pd_sync)
