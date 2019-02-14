import matplotlib.pyplot as plt

def plot_walking(pd_bva):
    plt.plot(pd_bva.position_x, pd_bva.position_y)
    plt.show()
    
def plot_position_histograms(pd_bva):
    fig, axes = plt.subplots(2)
    pd_bva.hist(column='position_x', bins=100, ax=0)
    pd_bva.hist(column='position_y', bins=100, ax=1)
