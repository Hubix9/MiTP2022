# Informacje ogólne
W folderze zawarłem gry:

- Zgadnij liczbę (guessTheNumber.py)
- Smocza kraina (LandOfDragons.py)
- Poszukiwanie skarbów (SonarSearch.py)
- Pong (Pong.py, gra działa, jest skończona w 99 %, musze tylko wprowadzić małe poprawki)
- Kółko i krzyżyk (jeszcze nie zaimplementowane)

Prawie wszystkie gry nie korzystają z zewnętrznych bibliotek, wyjątkiem jest Pong jednak odpowiednie biblioteki zostały zapakowane razem z grą, więc nic dodatkowego nie trzeba ściągać

Gry zostały przeznaczone dla systemu operacyjnego Windows 10 lub nowszego, Python wersja 3.7.6 lub nowsza.
Moduły pomocnicze wykorzystywane przez gry (folder common) zawierają również odniesienia do rodzin systemów Linux oraz MacOS, w związku z czym gry uruchamiają się na tych systemach, jednak działanie gier nie zostało przeze mnie wystarczająco przetestowane w tych środowiskach aby określić działanie gry w nich jako stabilne.
Dotyczy to przede wszystkim gry Pong która wykorzystuje zewnętrzną bibliotekę do obsługi klawiatury.

Poza główną logiką gier, zaimplementowałem również menu wraz z opcjami: wznowienia gry, pomocy, zapisu gry, wczytania gry oraz zamknięcia gry.

(Po wczytaniu gry należy ją wznowić, wczytanie gry nie wznawia jej automatycznie)

Zalecam uruchamianie gier poprzez wiersz poleceń Windows (cmd.exe) zamiast terminali wbudowanych do środowisk IDE, z uwagi na wykorzystanie 24-bitowego trybu kolorów do wyświetlania obrazów. W przypadku uruchomienia gry w terminalu nie obsługującym tego trybu kolorów, grafika nie zostanie wyświetlona poprawnie,
co może znacząco utrudnić bądź całkowicie uniemożliwić rozgrywkę.
W przypadku systemu MacOS zalecam korzystanie z terminalu "Iterm2", z uwagi na brak wsparcia trybu kolorów wykorzystywanego przez gry w domyślnym, systemowym terminalu. W systemach z rodziny Linux gry zostały sprawdzone na następujących terminalach: "xfce4-terminal", "gnome-terminal"

Aby uruchomić którąś z gier należy wykonać implementujący ją plik w interpreterze Pythona

przykładowe polecenie uruchamiające grę "Poszukiwanie skarbów": python SonarSearch.py

# Detale dotyczące poszczególnych gier

### Zgadnij liczbę
Aby uruchomić grę należy wykonać plik: "guessTheNumber.py"

Poprawnie działająca gra prezentuje się w następujący sposób:
TODO

### Smocza kraina
Aby uruchomić grę należy wykonać plik: "LandOfDragons.py"
W celu ułatwienia testów funkcjonalności gry, razem z grą jest dołączony zapis gry "rnd10.save", w tej rundzie smok w jaskini nr. 7 jest przyjazny co będzie skutkowało możliwością przetestowania czy da się wygrać grę. Zapis gry można wczytać za pośrednictwem menu, dostępnego po wpisaniu polecenia "menu".

Poprawnie działająca gra prezentuje się w następujący sposób:
TODO

### Poszukiwanie skarbów
Aby uruchomić grę należy wykonać plik: "SonarSearch.py"
W celu ułatwienia testów funkcjonalności gry, razem z grą jest dołączony zapis gry "tst2.save", w tym stanie rozgrywki 2 z 3 skrzyń zostały już zebrane, ostatnia skrzynia znajduje się w koordynatach: 19 11, co pozwoli na sprawdzenie czy gra posiada możliwość zwycięstwa. Zapis gry można wczytać za pośrednictwem menu, dostępnego po wpisaniu polecenia "menu".

Poprawnie działająca gra prezentuje się w następujący sposób:
TODO

### Pong
Aby uruchomić grę należy wykonać plik: "Pong.py"

Aby uruchomić menu w trakcie gry należy naciśnąć klawisz "m".

#### Known issues

- W niektórych sytuacjach piłka odbija się w tą samą stronę z której przyleciała
- W sytuacji gdy paletka oraz piłka jednocześnie zbliżają się do siebie, kolizja pomiędzy nimi może nie zostać wykryta

Poprawnie działająca gra prezentuje się w następujący sposób:
TODO


### Kółko i krzyżyk 
TODO