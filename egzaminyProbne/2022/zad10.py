# Copy rozni sie od deepcopy tym ze w przypadku kopiowania obiektu przechowujacego inne obiekty, jak np. klasa
# Copy utworzy nowa instancje tego obiektu, jednak obiekty ktore sa w nim przechowywane nie beda nowymi instancjami z wartosciami oryginalnych obiektow
# Beda to referencje do tych samych obiektow co w obiekcie pierwotnym
# W przypadku Deepcopy zostanie utworzona nowa instancja obiektu jak i obiektow w nim przechowywanych, dzialanie to jest rekursywne

from copy import copy, deepcopy

class Klasa:
    def __init__(self, lista):
        self.lista = lista


klasa = Klasa([1,2,3])
klasaKopia = copy(klasa)
klasaDeepKopia = deepcopy(klasa)
klasa.lista.remove(1)

print(f"obiekt lista klasy pierwotnej: {klasa.lista}")
print(f"obiekt lista klasy skopiowanej płytko (copy): {klasaKopia.lista}")
print(f"obiekt lista klasy skopiowanej gleboko (deepcopy): {klasaDeepKopia.lista}")

print("Jak widac modyfikacja oryginalnej listy wplynela rowniez na liste w skopiowanej plytko klasie"
      "\nNie zachodzi to jednak w klasie skopiowanej gleboko")