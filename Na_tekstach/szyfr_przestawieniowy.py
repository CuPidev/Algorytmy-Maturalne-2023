def szyfruj_pary(tekst):
    wynik = ""
    for i in range(0, len(tekst), 2):
        wynik += tekst[i+1]
        wynik += tekst[i]
    return wynik

print(szyfruj_pary("piotra"))