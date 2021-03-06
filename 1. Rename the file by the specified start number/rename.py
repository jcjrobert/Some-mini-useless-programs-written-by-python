from pathlib import Path

# Here input the start number you specified
start = 1

# Here input an absolute path of a source directory that you want to rename
path = Path(r'xx')

for i in path.iterdir():
    rename = f"{start}{i.name[i.name.find('.'):]}"
    i.rename(path / rename)
    start += 1