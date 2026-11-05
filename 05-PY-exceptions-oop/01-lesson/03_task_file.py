from pathlib import Path

path = Path.cwd().parent / "data"
filename = path / "report.txt"

try:
    with filename.open("w", encoding="utf-8") as file:
        file.write("Practice report\n")
except PermissionError:
    print("Du har ikke tilgang twil å skrive til filen")

