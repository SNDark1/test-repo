часть 1


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




     часть 2


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        current_value = arr[i]
        j = i -1
        while j >= 0 and arr[j] > current_value:
            arr[j+ 1] = arr[j]
            j-= 1
            arr[j + 1] = current_value

array = [27, 83, 52.3, 0, 19, 35, 41]
insertion_sort(array)
print('отсортированный массив:')
print(array)
