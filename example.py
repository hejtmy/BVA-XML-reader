from bvareader import reader
from bvareader import plotter 
from bvareader import preprocessing

pd_bva = reader.read_xml_bva("example_data/example.xml")
plotter.plot_triangle(pd_bva, 1000)

pd_bva2 = preprocessing.preprocess_bva_data(pd_bva)
pd_bva = preprocessing.add_rotation(pd_bva)

reader.save_csv(pd_bva2, "bva.csv")
reader.save_csv(pd_bva, "bva_full.csv")

pd_sync = reader.read_sync_file("example_data/example.csv")
reader.save_csv(pd_sync, "sync.csv")
