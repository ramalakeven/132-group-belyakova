import time
import random

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

if __name__ == '__main__': 
    arr = [random.randint(0, 999999) for _ in range(50000000)]

    start_time = time.time()
    quick_sort(arr, 0, len(arr) - 1)
    end_time = time.time()

    print(f"Время выполнения быстрой сортировки: {end_time - start_time} секунд")
