textInput = input("Podaj trzy liczby: ")
numbers = textInput.split(",")
numbers = [int(x) for x in numbers] # Fun fact, python przy konwersji stringa na int pomija spacje, "    23" przekonwertuje sie tak samo jak "23"
# Stad w splicie moge dzielic po przecinku
print(f"Wsrod liczb {numbers[0]}, {numbers[1]} i {numbers[2]} maksymalna to: {max(numbers)}!")