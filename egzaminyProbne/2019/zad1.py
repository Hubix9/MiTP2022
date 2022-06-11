# Bmi
from math import floor

name = input("Podaj swoje imie: ")
weight = int(input("Podaj swoja wage: "))
height = int(input("Podaj swoj wzrost: ")) / 100

bmi = weight/(height**2)

print(f"{name}, Twoje BMI to {round(floor(bmi * 10)/10, 1)}!") #Mnoze razy 10 i po zaokragleniu w dol dziele przez 10, zeby nie zgubic cyfr po przecinku
