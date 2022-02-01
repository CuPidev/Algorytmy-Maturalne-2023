def szuaknie_binarne(arr, t):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == t:
            return mid
        elif arr[mid] < t:
            left = mid + 1
        else:
            right = mid - 1


print(szuaknie_binarne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
