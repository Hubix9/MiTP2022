# except Valuerror ->in<- valerr: Powinno tutaj byc "as" zamiast "in"
# ostatnia linijka nie posiada dwokropka
# znaki == przy przypisaniu wartosci do zmiennych numbers oraz result

#Ponizej poprawiony kod
while True:
    try:
        numbers = input("Podaj:").split(",")
        result = int(numbers[0]) / int(numbers[1])
        print("Iloraz", result)
    except ZeroDivisionError:
        print("Nie dziel przez zero!")
    except ValueError as valerr:
        print("Podano bledne dane:", valerr)
    except:
        print("Wystapil blad.")
    else:
        break
