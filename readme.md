# BVA reader
Python package which reads and parses xml data from LF in Motol.

## Installation
The project is currently hosted on test PyPi and can be downloaded from such
[https://test.pypi.org/project/bvareader/](https://test.pypi.org/project/bvareader/)


## Use examples
Main use can be through the command line prompts, which doesn't require you to run your own preprocessing scripts. But if you prefer, you can preprocess and save the data in your own way.

```python
from bvareader.reader import read_positions
from bvareader.reader import read_sync_times
from bvareader.reader import read_sync_file
from bvareader.exporter import save_csv

from bvareader.preprocessing import prepare_positions
from bvareader.preprocessing import add_rotation

pd_bva = read_positions("example_data/example.xml")
pd_bva_clean = prepare_positions(pd_bva)

save_csv(pd_bva_clean, "bva.csv")
save_csv(pd_bva, "bva_full.csv")

bva_sync = read_sync_times("example_data/example.xml")
save_csv(pd_sync, "bva_sync.csv")

pd_sync = read_sync_file("example_data/example.csv")
save_csv(pd_sync, "sync.csv")
```

#### Timestamp
Bva outputs real timestamp (date and time of each recording). This package converts this datetime number as the POSIX timestamp (number of seconds since 1.1.1970) as per `datetime.timestamp()` function described in [here](https://docs.python.org/3/library/datetime.html#datetime.datetime)

## Command line prompt
By installing the package from PyPI, you will get the python entry point which you can use in the command line. You can investigate each command with the `--help` tag. e.g. `process-bva --help`. Mostly you will need only the `process-bva` and potentially `xml-settings-to-csv` commands

BVA xml output preprocessing
```bash
process-bva "path_to_xml" -o/--output "output-prefix"
bva-positions "path_to_xml" -o/--output "output-prefix"
bva-phases "path_to_xml" -o/--output "output-prefix"
bva-measures-start-stop "path_to_xml" -o/--output "output-prefix"
bva-sync-times "path_to_xml" -o/--output "output-prefix"
xml-settings-to-csv "path_to_xml" -o/--output "output-prefix"
```

### FAQ
Q: The command line commands are not found.

A: If you are using conda or virtual envs, make sure you are in a correct environment