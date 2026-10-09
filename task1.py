import sys
import time
import random
import matplotlib.pyplot as plt

sys.setrecursionlimit(10000)

def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

time_sel_random, time_quick_random = [], []
time_sel_sorted, time_quick_sorted = [], []
time_sel_reverse, time_quick_reverse = [], []

for n in sizes:
    arr_random = [random.randint(0, 10000) for _ in range(n)]
    arr_sorted = list(range(n))
    arr_reverse = list(range(n, 0, -1))

    start = time.perf_counter()
    selection_sort(arr_random[:])
    time_sel_random.append(time.perf_counter() - start)

    start = time.perf_counter()
    quicksort(arr_random[:])
    time_quick_random.append(time.perf_counter() - start)

    start = time.perf_counter()
    selection_sort(arr_sorted[:])
    time_sel_sorted.append(time.perf_counter() - start)

    start = time.perf_counter()
    quicksort(arr_sorted[:])
    time_quick_sorted.append(time.perf_counter() - start)

    start = time.perf_counter()
    selection_sort(arr_reverse[:])
    time_sel_reverse.append(time.perf_counter() - start)

    start = time.perf_counter()
    quicksort(arr_reverse[:])
    time_quick_reverse.append(time.perf_counter() - start)

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

axes[0].plot(sizes, time_sel_random, label='Сортировка выбором', marker='o')
axes[0].plot(sizes, time_quick_random, label='Быстрая сортировка', marker='s')
axes[0].set_title('Случайный список')
axes[0].set_xlabel('Размер массива')
axes[0].set_ylabel('Время (сек)')
axes[0].legend()
axes[0].grid(True)

axes[1].plot(sizes, time_sel_sorted, label='Сортировка выбором', marker='o')
axes[1].plot(sizes, time_quick_sorted, label='Быстрая сортировка', marker='s')
axes[1].set_title('Отсортированный список')
axes[1].set_xlabel('Размер массива')
axes[1].set_ylabel('Время (сек)')
axes[1].legend()
axes[1].grid(True)

axes[2].plot(sizes, time_sel_reverse, label='Сортировка выбором', marker='o')
axes[2].plot(sizes, time_quick_reverse, label='Быстрая сортировка', marker='s')
axes[2].set_title('Обратный список')
axes[2].set_xlabel('Размер массива')
axes[2].set_ylabel('Время (сек)')
axes[2].legend()
axes[2].grid(True)

plt.tight_layout()
plt.show()