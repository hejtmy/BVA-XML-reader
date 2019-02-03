%load_ext autoreload
%autoreload 2

import matplotlib.pyplot as plt
from functions.bva_xml_reader import read_xml
from functions.bva_sync_reader import read_sync_file

pd_bva, pd_times = read_xml("example_data/example.xml")
save_csv(pd_bva, "bva.csv")

plt.plot(pd_bva.PointX, pd_bva.PointY)

pd_sync = read_sync_file("example_data/example.csv")
save_csv(pd_sync, "sync.csv")