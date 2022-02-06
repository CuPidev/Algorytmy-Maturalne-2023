# Metoda rekurencyjna
def szybkie_potegowanie(podstawa, wykladnik):
    if wykladnik == 0:
        return 1
    x = szybkie_potegowanie(podstawa, wykladnik // 2)
    x = x * x
    if wykladnik % 2 == 1:
        x = x * podstawa
    return x


# Metoda iteracyjna
def szybkie_potegowanie_iteracyjne(podstawa, wykladnik):
    x = 1
    while wykladnik > 0:
        if wykladnik % 2 == 1:
            x = x * podstawa
        podstawa = podstawa * podstawa
        wykladnik = wykladnik // 2
    return x
