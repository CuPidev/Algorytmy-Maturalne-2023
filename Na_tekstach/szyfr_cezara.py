def szyfruj_cezar(tekst, klucz):
    wynik = ""
    for i in tekst:
        temp = chr(ord(i) + klucz % 26)
        wynik += temp
    return wynik

print(szyfruj("piotr", 3))