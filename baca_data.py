# Membaca Berkas CSV (baca_data.py) #
import csv

data = []
with open("nilai.csv") as f:
    reader = csv.DictReader(f)
    for baris in reader:
        baris["nilai"] = int(baris["nilai"])
        data.append(baris)

print(len(data), "baris")
print(data[0])
