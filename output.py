# Format Output dengan print() (output.py) #
print("Halo", "Dunia")
print("A", "B", "C", sep="-")
print("Loading", end="...")
print("selesai")

harga = 1500000 / 7
print(f"Harga: Rp{harga:.2f}")
print(f"Total: {1500000:,}")