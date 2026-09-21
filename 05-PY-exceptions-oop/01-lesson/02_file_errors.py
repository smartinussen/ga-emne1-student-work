import encodings
from pathlib import Path

data_folder = Path.cwd().parent / "data"
datafile = data_folder / "message.txt"

try:
    with datafile.open(encoding="utf-8") as file:  # path.open (opens designated file)
        messsage = file.read()
    print(messsage)
except FileNotFoundError:
    print(f"The file {datafile.name} does not exist in {data_folder}")

####

data_folder = Path(__file__).parent.parent / "data"
numberfile = data_folder / "number.txt"

try:
    with numberfile.open(encoding="utf-8") as filer:
        number = int(filer.read().strip())
        print(number*2)
except FileNotFoundError:
    print(f"The file {numberfile.name} does not exist in {data_folder}")
except ValueError:
    print("The file must contain an integer")