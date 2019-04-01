import matplotlib.pyplot as plt

def plot_walking(pd_bva):
    plt.plot(pd_bva.Point_x, pd_bva.Point_y)
    plt.show()


def plot_position_histograms(pd_bva):
    fig, axes = plt.subplots(2)
    pd_bva.hist(column='Point_x', bins=100, ax=0)
    pd_bva.hist(column='Point_y', bins=100, ax=1)


def plot_triangle(pd_bva, index):
  plt.scatter(pd_bva.Front_x[index], pd_bva.Front_y[index], marker='o', s=5)
  plt.scatter(pd_bva.Right_x[index], pd_bva.Right_y[index], marker='o', s=5)
  plt.scatter(pd_bva.Left_x[index], pd_bva.Left_y[index], marker='o', s=5)
  plt.show()