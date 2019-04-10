# BVA reader
Python package which reads and parses xml data from LF in Motol.

## Use examples
Main use can be through the command line prompts, which doesn't require you to run your own preprocessing scripts. But if you prefer, you can preprocess and save the data in your own way.

```python
from bvareader.reader import read_xml_bva
from bvareader.reader import read_xml_sync
from bvareader.reader import read_sync_file
from bvareader.reader import save_csv

from bvareader.preprocessing import preprocess_bva_data
from bvareader.preprocessing import add_rotation

pd_bva = read_xml_bva("example_data/example.xml")
pd_bva_clean = preprocess_bva_data(pd_bva)
pd_bva = add_rotation(pd_bva)

save_csv(pd_bva_clean, "bva.csv")
save_csv(pd_bva, "bva_full.csv")

pd_sync = read_sync_file("example_data/example.csv")
save_csv(pd_sync, "sync.csv")
```

### Plotting

## Command line prompt
By installing the package from PyPI, you will get the python entry point which you can use in the command line.

```python
bva-preprocess-xml "path_to_xml" "path_to_output_without_extension"
```

### FAQ
Q: The command line commands are not found.

A: If you are using conda or virtual envs, make sure you are in a correct environment before.