def wyszukanie_wzorca_naiwne(array, target):
    dl_a = len(array)
    dl_t = len(target)
    p = 0
    while(p<=dl_a - dl_t):
        i = 0
        while(i<dl_t and array[p+i] == target[i]):
            i += 1
        if i == dl_t:
            return p, p+dl_t-1
        else:
            p = p+1
    return -1

testowy_tekst = "piotrbrzeczyszczykiewicz"
testowy_wzorzec = "pio"
print(wyszukanie_wzorca_naiwne(testowy_tekst, testowy_wzorzec))
    