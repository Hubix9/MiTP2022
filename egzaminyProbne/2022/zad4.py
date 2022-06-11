f = open("piosenkiBiebera.txt")

lines = f.readlines() # zwraca liste stringow ktore sa posczegolnymi liniami pliku

print(f"liczba linii: {len(lines)}")
print(f"najdluzsza linia to: {max(lines, key=len)}")

