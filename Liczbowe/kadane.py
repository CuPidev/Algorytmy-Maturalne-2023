# Algorytm Kadane'a służy do optymalnego rozwiązania problemu znajdowania podciągu o największej sumie. Działa on jedynie w przypadku gdy suma jest dodatnia.
# Złożoność czasowa: O(n)


def maximum_sum_subarray(array):
    max_sum = 0
    current_sum = 0

    max_start = 0
    max_end = 0
    current_start = 0
    current_end = 0

    for i in range(len(array)):
        current_sum = current_sum + array[i]
        current_end = i
        if current_sum < 0:
            current_sum = 0
            current_start = current_end + 1
        if max_sum < current_sum:
            max_sum = current_sum
            max_start = current_start
            max_end = current_end
    return max_sum, max_start, max_end


testowa_tablica = [-100, 2, -3, -8, -11, -12, -19, -62, -3, -1, -2]
print(maximum_sum_subarray(testowa_tablica))
