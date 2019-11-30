import matplotlib.pyplot as plt
from bvareader.preprocessing import calculate_perpendicular_cross


def plot_walking(pd_bva):
    plt.plot(pd_bva.Point_x, pd_bva.Point_y)
    plt.show()


def plot_position_histograms(pd_bva):
    fig, axes = plt.subplots(2)
    pd_bva.hist(column='Point_x', bins=100, ax=0)
    pd_bva.hist(column='Point_y', bins=100, ax=1)


def plot_triangle(pd_bva, index):
    line = pd_bva.iloc[index]
    plot_triangle_height(line.Left_x, line.Left_y, line.Right_x, line.Right_y, line.Front_x, line.Front_y)


def plot_triangle_height(x1, y1, x2, y2, top_x, top_y):
    plt.scatter(top_x, top_y, marker='o', s=10)
    plt.scatter(x1, y1, marker='o', s=10)
    plt.scatter(x2, y2, marker='o', s=10)
    cross_x, cross_y = calculate_perpendicular_cross(x1, y1, x2, y2, top_x, top_y)
    plt.scatter(cross_x, cross_y, marker='o', s=10)
    plt.plot([cross_x, top_x], [cross_y, top_y], lw=1)
    plt.plot([x1, x2], [y1, y2], lw=1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
