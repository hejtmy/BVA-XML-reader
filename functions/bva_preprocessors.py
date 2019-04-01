import pandas as pd
import numpy as np


# Removes any points that are out of constraints of the bva and replaces then with NAs
def clear_out_of_arena_positions(pd_bva):
    pd_bva.Point_x[np.abs(pd_bva.Point_x) > 250] = np.nan
    pd_bva.Point_y[np.abs(pd_bva.Point_y) > 250] = np.nan
    return(pd_bva)


def add_rotation(pd_bva):
  x_cross, y_cross = calculate_perpendicular_cross(pd_bva.Left_x, pd_bva.Left_y, pd_bva.Right_x, pd_bva.Right_y, pd_bva.Front_x, pd_bva.Front_y)
  front_x, front_y = pd_bva.Front_x - x_cross, pd_bva.Front_y - y_cross
  zipped = list(zip(front_x, front_y))
  pd_bva['rotation'] = angle_between(zipped, [(0,1)])
  return(pd_bva)


## Calculates the perpendicular line to left and right point line which goes through front
def calculate_perpendicular_cross(x1, y1, x2, y2, x3, y3):
  k = ((y2-y1) * (x3-x1) - (x2-x1) * (y3-y1)) / (np.square(y2-y1) + np.square(x2-x1))
  x4 = x3 - k * (y2-y1)
  y4 = y3 + k * (x2-x1)
  return(x4, y4)


def navr_output(pd_bva):
  pd_navr_bva = pd_bva
  return(pd_navr_bva)


# p1 are lists of touples [(0,1),(1,0)]
def angle_between(p1, p2):
  x, y = zip(*p1[::1])
  ang1 = np.arctan2(x, y)
  x, y = zip(*p2[::1])
  ang2 = np.arctan2(x, y)
  degrees = np.rad2deg((ang1 - ang2) % (2 * np.pi))
  return(degrees)

