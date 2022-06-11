# Wartosci wypisane
# 1 Justin 1 Bieber 4 Justin 4 Bieber

# i przyjmie wartosc 1993
# j przyjmie wartosc "Bieber


for i in range(1,1994,3):
    for j in ['Justin','Bieber']:
        if i < len(j):
            print(i,j,end=" ")

print("\nwartosci i oraz j")
print(i, j)