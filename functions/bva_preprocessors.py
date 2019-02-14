import pandas as pd
import numpy as np

# Removes any points that are out of constraints of the bva and replaces then with NAs
def clear_out_of_arena_positions(pd_bva):
    pd_bva.position_x[np.abs(pd_bva.position_x) > 250] = np.nan
    pd_bva.position_y[np.abs(pd_bva.position_y) > 250] = np.nan
    return(pd_bva)