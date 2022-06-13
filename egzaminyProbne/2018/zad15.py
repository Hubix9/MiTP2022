# F
# E
# G
# J
# C
# I
# A
# H
# D

# Gotowy kod
while True:
    try:
        num1, num2 = input("Podaj:").split(",")
        result = int(num1) / int(num2)
    except:
        print("Bledne dane.")
        break
    else:
        print("Iloraz", result)
