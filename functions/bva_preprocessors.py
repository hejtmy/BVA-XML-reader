import pandas as pd
import numpy as np

# Removes any points that are out of constraints of the bva and replaces then with NAs
def clear_out_of_arena_positions(pd_bva):
    pd_bva.Point_x[np.abs(pd_bva.Point_x) > 250] = np.nan
    pd_bva.Point_y[np.abs(pd_bva.Point_y) > 250] = np.nan
    return(pd_bva)

def add_rotation(pd_bva):
  return(pd_bva)

def navr_output(pd_bva):
  pd_navr_bva = pd_bva
  return(pd_navr_bva)