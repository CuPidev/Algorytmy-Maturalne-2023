def wyszukiwanie_liniowe(array, t):
    for i in range(len(array)):
        if array[i] == t:
            return i
    return -1  
        
testowa_tablica = [1, 5, 8, 13, 15, 156, 12]
t = 15
print(wyszukiwanie_liniowe(testowa_tablica, t))