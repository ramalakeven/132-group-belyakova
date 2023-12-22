import random
import time

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == '__main__':
    arr = [random.randint(0, 999999) for _ in range(50000000)]

    start_time = time.time()
    bubble_sort(arr)
    end_time = time.time()

    print(f"Время выполнения пузырьковой сортировки: {end_time - start_time} секунд")
