import time
import random
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

if __name__ == '__main__': # оно жесть какое долгое бесконечное так что я не уверена что оно работает дальше как надо или как то по другому надо было сделать
    arr = [random.randint(0, 999999) for _ in range(50000000)]

    start_time = time.time()
    merge_sort(arr)
    end_time = time.time()

    print(f"Время выполнения сортировки слиянием: {end_time - start_time} секунд")
