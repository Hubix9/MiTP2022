# num1; num2 <- srednik jest bledem, zamist niego powinien zostac wstawiony przecinek,
# ktory sluzy do oddzielania zmiennych w trakcie przypisywania wielu wartosci

# zmienna score nie istnieje, w wywolaniu print("Iloraz", score), mozna ja zastapic zmienna result

# true w pierwszej linijce jest z malej litery, powinno byc z duzej

while True:
    try:
        num1, num2 = input("Podaj:").split(",")
        result = int(num1) / int(num2)
    except ZeroDivisionError:
        print("Nie dziel przez zero!")
    except ValueError as valerr:
        print("Podano bledne dane:", valerr)
    except: print("Wystapil blad.")
    else:
        print("Iloraz", result)
        break