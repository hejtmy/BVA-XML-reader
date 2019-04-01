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
def calculate_perpendicular_cross(line1_x, line1_y, line2_x, line2_y, origin_x, origin_y):
  k = (((line2_y-line1_y) * (origin_x-line1_x)) - ((line2_x-line1_x) * (origin_y-line1_y))) / (np.square(line2_y-line1_y) + np.square(line2_x-line1_x))
  x4 = origin_x - (k * (line2_y-line1_y))
  y4 = origin_y + (k * (line2_x-line1_x))
  return(x4, y4)


def calculate_perpendicular_cross_classical(line1_x, line1_y, line2_x, line2_y, origin_x, origin_y):
  slope = (line2_x - line1_x) / (line2_y - line1_y)
  b = line1_y + line1_x * slope
  perp_slope = (line1_y - line2_y) / (line2_x - line1_x)
  perp_b = origin_y + (perp_slope * origin_x) #linear coef B
  cross_x = (perp_b - b)/(slope-perp_slope)
  cross_y = perp_slope*cross_x + perp_b
  return(cross_x, cross_y)


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

