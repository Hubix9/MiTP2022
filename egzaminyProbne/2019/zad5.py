# C nie pasuje bo pusty dictionary jest wartoscia ewaluowana logicznie jako falsz


#Konwertuje niektore z wartosci na boolean aby wyswietlic ich wartosc logiczna, a nie ich rzeczywista wartosc jak np. 42
print("A:", bool(42))
print("B:", bool("Bieber"))
print("C:", bool({}))
print("D:", True or not True)




