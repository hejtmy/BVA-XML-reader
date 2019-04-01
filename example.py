from bvareader.reader import save_csv
from bvareader.reader import read_xml_bva
from bvareader.reader import read_xml_sync
from bvareader.reader import read_sync_file
from bvareader.plotter import plot_triangle
from bvareader.preprocessing import preprocess_bva_data
from bvareader.preprocessing import add_rotation

pd_bva = read_xml_bva("example_data/example.xml")
plot_triangle(pd_bva, 1000)

pd_bva2 = preprocess_bva_data(pd_bva)
pd_bva = add_rotation(pd_bva)

save_csv(pd_bva2, "bva.csv")
save_csv(pd_bva, "bva_full.csv")

pd_sync = read_sync_file("example_data/example.csv")
save_csv(pd_sync, "sync.csv")
