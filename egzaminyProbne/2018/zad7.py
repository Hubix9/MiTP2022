# A nie pasuje, wyrazenie zawsze bedzie falszywe
a, b = True, True #niezaleznie od wartosci logicznej a i b, wyrazenie A bedzie zawsze falszywe
print("A: ", (a or b) and not (a or b))
print("B: ", True)
print("C: ", (a or not a) or False)
print("D: ", bool(5)) # Wykonuje konwersje wartosci 5 na wartosc zerojedynkowa (prawda / fałsz), inaczej program wyswietli po prostu 5