import pandas as pd
import xml.etree.ElementTree as ET
from bvareader.new_bva.helpers import real_timestamp, flatten_list, element_to_row


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
    pd_times = pd.DataFrame(data={'timestamp': times})
    return(pd_times)


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


def read_measure_start_stop(path):
    root = ET.parse(path).getroot()
    start_times, stop_times, i_phases = [], [], []
    i_phase = 0  # raised to 1 in the first phase
    for phase in root.iter('Phase'):
        i_phase += 1
        measures_starts = phase.findall("./MousePath/MeasureStartItem")
        measures_stops = phase.findall("./MousePath/MeasureStopItem")
        if(len(measures_starts) < 1):
            continue
        if(len(measures_starts) != len(measures_stops)):
            # raise Exception('there is unequal number of start measures and stop measures')
            start_times += [float("NaN")]
            stop_times += [float("NaN")]
            i_phases += [str(i_phase)]
        else:
            phase_timestamp = real_timestamp(phase.find("./MousePath/TimestampPoint"))
            for n in range(0, len(measures_starts)):
                start_times += [float(measures_starts[n].find("Timestamp").text) + phase_timestamp]
                stop_times += [float(measures_stops[n].find("Timestamp").text) + phase_timestamp]
                i_phases += [str(i_phase)]
    pd_start_stops = pd.DataFrame(data={'measure_start': start_times, 'measure_stop': stop_times,
                                        'phase_number': i_phases})
    return pd_start_stops


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
    pd_sync.time = (pd.to_datetime(pd_sync.time, format='%H:%M:%S') -
                    pd.to_datetime("00:00:00", format='%H:%M:%S')).dt.total_seconds()
    pd_sync.time = pd_sync.time + pd_sync.ms / 1000
    return(pd_sync)