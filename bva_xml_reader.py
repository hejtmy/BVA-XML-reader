import pandas as pd
import xml.etree.ElementTree as ET

def read_xml(path):
    root = ET.parse(path).getroot()
    POINTS = ['Point', 'Front', 'Left', 'Right']
    phase_times = []
    mat = []
    continuous_time = 0
    for phase in root.iter('Phase'):
        phase_times.append([continuous_time,"PhaseStart"])
        phase_time = 0
        for TimestampPoint in phase.iter('TimestampPoint'):
            phase_time = float(TimestampPoint.find('Timestamp').text)
            temp = []
            temp.append(phase_time + continuous_time)
            for point in POINTS:
                xy = TimestampPoint.find(point)
                temp.append(float(xy.find('X').text))
                temp.append(float(xy.find('Y').text))
            mat.append(temp)
        continuous_time += phase_time

    pd_phases = pd.DataFrame(phase_times, columns=["Timestamp","Event"])
    pd_bva = pd.DataFrame(mat, columns=['Timestamp', 'PointX', 'PointY', 'FrontX', 'FrontY',
                                        'LeftX', 'LeftY', 'RightX', 'RightY'])
    return(pd_bva, pd_phases)

def preprocess_data(pd_data):
    return(True)

