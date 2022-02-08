def babelkowe(array):
    for i in range(len(array)):
        swapped = False
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                
                swapped = True
        if not swapped:
            break
    
        
testowa_tablica = [2, 8, 11, 3, 16, 5, 4, 9, 10, 14, 13, 12]
babelkowe(testowa_tablica)
print(testowa_tablica)