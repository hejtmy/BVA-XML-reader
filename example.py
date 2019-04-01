import matplotlib.pyplot as plt
from functions.bva_xml_reader import save_csv
from functions.bva_xml_reader import read_xml_bva
from functions.bva_xml_reader import read_xml_sync
from functions.bva_xml_reader import read_xml_phases
from functions.bva_sync_reader import read_sync_file
from functions.bva_plotting import plot_triangle
from functions.bva_preprocessors import preprocess_bva_data
from functions.bva_preprocessors import add_rotation

pd_bva = read_xml_bva("example_data/example.xml")
plot_triangle(pd_bva, 1000)

pd_bva2 = preprocess_bva_data(pd_bva)
pd_bva = add_rotation(pd_bva)

save_csv(pd_bva2, "bva.csv")
save_csv(pd_bva, "bva_full.csv")

pd_sync = read_sync_file("example_data/example.csv")
save_csv(pd_sync, "sync.csv")
