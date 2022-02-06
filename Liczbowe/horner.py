def horner(wspolczynniki, ilosc_wspolczynnikow, argument):
    wynik = wspolczynniki[0]
    for i in range(1, ilosc_wspolczynnikow):
        wynik = wynik * argument + wspolczynniki[i]
    return wynik


wsp = [2, 4, 5, 6]
x = 3
n = len(wsp)

print(horner(wsp, n, x))
