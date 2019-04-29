import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime
from bvareader.helpers import flatten_list
from bvareader.helpers import find_duplicates
from bvareader.helpers import remove_at_indices


def read_xml_phases(path):
    root = ET.parse(path).getroot()
    phase_times = []
    i_phase = 1
    for phase in root.iter('Phase'):
        row = [str(i_phase)]
        # phase_time = 0
        tps = phase.findall("./MousePath/TimestampPoint")
        if len(tps) == 0:
            row += [float('nan'), float('nan'), float('nan')]
        else:
            row.append(real_timestamp(tps[0]))
            row.append(real_timestamp(tps[-1]))
            row.append(float(tps[-1].find('Timestamp').text))
        phase_times.append(row)
        i_phase += 1
    pd_phases = pd.DataFrame(phase_times, columns=["phase_number", "timestamp_start", 
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
    # adds colnames for all the points
    colnames = ['timestamp_bva', 'timestamp'] + (flatten_list([[x + "_x", x + "_y"] for x in POINTS]))
    pd_bva = pd.DataFrame(bva_mat, columns=colnames)
    return(pd_bva)


def read_xml_settings(path):
    root = ET.parse(path).getroot()
    pd_settings = pd.DataFrame()
    i_phase = 1
    for phase in root.iter('phase'):
        keys, values = element_to_row(phase)
        keys += ["phase_number"]
        values += [str(i_phase)]
        # Check if the keys are still the same and values of the same length
        pd_row = pd.DataFrame([values], columns=keys)
        pd_settings = pd.concat([pd_settings, pd_row])
        i_phase += 1
    return pd_settings


def read_sync_file(path):
    pd_sync = pd.read_csv(path, sep=",")
    pd_sync.time = (pd.to_datetime(pd_sync.time, format='%H:%M:%S') - pd.to_datetime("00:00:00", format='%H:%M:%S')).dt.total_seconds()
    pd_sync.time = pd_sync.time + pd_sync.ms / 1000
    return(pd_sync)


#' Heavilly needs description
def element_to_row(element):
    keys = flatten_list([[element.tag + "_" + x] for x in list(element.attrib.keys())])
    values = list(element.attrib.values())
    for el in element:
        tag = el.tag
        tag_keys = list(el.attrib.keys())
        keys += flatten_list([[tag + "_" + x] for x in tag_keys])
        tag_values = list(el.attrib.values())
        values += tag_values
        value = el.text
        if value is not None:
            keys += [tag + "_value"]
            values += [str(value)]
        children_keys, child_values = element_to_row(el)
        keys, values = keys + children_keys, values + child_values
    i_duplicate = find_duplicates(keys)
    keys, values = remove_at_indices(keys, i_duplicate), remove_at_indices(values, i_duplicate)
    return keys, values


#' Converts XML BVA timestamp to POSIX timestamp
def real_timestamp(element):
    # timestamp real is in form of 01/29/2019 10:02:45.574
    dt = datetime.strptime(element.find('TimestampReal').text,
                           '%m/%d/%Y %H:%M:%S.%f')
    return(float(dt.timestamp()))


#' Wrapper around 
def save_csv(pd_bva, path, dec_points=4):
    f = '%.'+str(dec_points)+'f'
    pd_bva.to_csv(path, sep=";", index=False, float_format=f)