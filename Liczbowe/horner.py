def horner(wspolczynniki, ilosc_wspolczynnikow, argument):
    wynik = wspolczynniki[0]
    for i in range(1, ilosc_wspolczynnikow):
        wynik = wynik * argument + wspolczynniki[i]
    return wynik
