# Dziedziczenie, przeniesienie metod wykorzystanych w istniejacej juz klasie, do nowej
# Widoczne to jest w przypadku Klas Bieber oraz Mendes, obie dziedzicza z klasy Singer

# Metody specjalne jak __init__ (konstruktor) lub __len__, wplywaja one na dzialanie klasy w trakcie jej interakcji z innymi elementami jezyka, np. metoda init wywolywana w trakcie inicjalizacji metody

# Polimorfizm metod, Klasy Bieber oraz Mendes, obie posiadaja zmodyfikowane wersje metody sing z klasy z ktorej dziedzicza, dzieki temu za pomoca wspolnego interfejsu mozna zapewnic odpowiednio dostosowane do operacji dzialanie metod.
# Metoda sing jest wykorzstywana na koncu pliku pomimo ze Bieber i Mendes to dwie rozne klasy

# Enkapsulacja, mozliwosc zawiarcia innych obiektow w klasach, widzimy to w metodzie __init__ klasy Singer, gdzie w klasie zostaja zapisane wartosci przekazane w parametrach metody
