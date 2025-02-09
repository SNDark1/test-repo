
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

