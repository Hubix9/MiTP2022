def is_square(apositiveint):
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True

strInput = input("Wprowadz liczbe: ")
try:
    number = int(strInput)
except:
    print("Niepoprawna wartosc")
    quit()

if number <= 0:
    print("Niepoprawna wartosc")
    quit()

if is_square(number):
    print("Liczba posiada calkowity pierwiastek kwadratowy")
else:
    print("Liczba nie posiada calkowitego pierwiastka kwadratowego")