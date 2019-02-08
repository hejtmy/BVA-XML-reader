import matplotlib.pyplot as plt

def plot_walking(pd_bva):
    plt.plot(pd_bva.PointX, pd_bva.PointY)
    plt.show()
    
def plot_position_histograms(pd_bva):
    fig, axes = plt.subplots(2)
    pd_bva.hist(column='PointX', bins=100, ax=0)
    pd_bva.hist(column='PointY', bins=100, ax=1)
