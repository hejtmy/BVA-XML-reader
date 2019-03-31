import matplotlib.pyplot as plt
from functions.bva_xml_reader import save_csv
from functions.bva_xml_reader import read_xml_bva
from functions.bva_xml_reader import read_xml_sync
from functions.bva_xml_reader import read_xml_phases
from functions.bva_sync_reader import read_sync_file

pd_bva = read_xml_bva("example_data/example.xml")

save_csv(pd_bva, "bva.csv")

plt.plot(pd_bva.Point_x, pd_bva.Point_y)

pd_sync = read_sync_file("example_data/example.csv")
save_csv(pd_sync, "sync.csv")