def genderPrediction(name):
    if name[-1].lower() == "a":
        return "Kobieta"
    else:
        return "Mezczyzna"

print(genderPrediction("Stachura"))
print(genderPrediction("Wiśniewski"))
print(genderPrediction("Kluza"))