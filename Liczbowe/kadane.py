# Algorytm Kadane'a służy do optymalnego rozwiązania problemu znajdowania podciągu o największej sumie.
# Złożoność czasowa: O(n)


def maximum_sum_subarray(array):
    max_sum = 0
    current_sum = 0
    for i in array:
        current_sum = current_sum + i
        if current_sum < 0:
            current_sum = 0
        if max_sum < current_sum:
            max_sum = current_sum
    return max_sum


testowa_tablica = [1, -2, 3, 8, 11, 12, -19, 12, 3, 1, 2]
print(maximum_sum_subarray(testowa_tablica))
