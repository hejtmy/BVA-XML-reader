import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

def read_xml(path):
    root = ET.parse(path).getroot()
    # Older versions had multiple points
    # POINTS = ['Point', 'Front', 'Left', 'Right']
    POINTS = ['Point']
    phase_times = []
    mat = []
    continuous_time = 0
    for phase in root.iter('Phase'):
        phase_times.append([continuous_time,"PhaseStart"])
        phase_time = 0
        for TimestampPoint in phase.iter('TimestampPoint'):
            # old points had only Timestamp
            phase_time = float(TimestampPoint.find('Timestamp').text)
            #timestamp real is in form of 01/29/2019 10:02:45.574
            dt = datetime.strptime(TimestampPoint.find('TimestampReal').text, '%m/%d/%Y %H:%M:%S.%f')
            phase_datetime_real = float(dt.timestamp())
            temp = []
            temp.append(phase_time + continuous_time)
            temp.append(phase_datetime_real)
            for point in POINTS:
                xy = TimestampPoint.find(point)
                temp.append(float(xy.find('X').text))
                temp.append(float(xy.find('Y').text))
            mat.append(temp)
        continuous_time += phase_time

    pd_phases = pd.DataFrame(phase_times, columns=["Timestamp", "Event"])
    pd_bva = pd.DataFrame(mat, columns=['Timestamp', 'TimestampReal', 'PointX', 'PointY'])
    #pd_bva = pd.DataFrame(mat, columns=['Timestamp', 'PointX', 'PointY', 'FrontX', 'FrontY', 'LeftX', 'LeftY', 'RightX', 'RightY'])
    return(pd_bva, pd_phases)


def save_csv(pd_bva, path):
    pd_bva.to_csv(path, sep=";", index=False)
