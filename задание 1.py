def search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right ) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            left = mid - 1
    return -1

arr = [3, 19, 23, 32, 41, 64, 87]
x = 19
result = search(arr, x)
if result != 1:
   print(f'элемент {x} найден на позиции {result}')
else:
    print(f'элемент {x} не найден')

