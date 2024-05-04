import timeit
import random


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Порівняння часу виконання для алгоритмів сортування на різних наборах даних
for size in [1000, 10000]:
    arr = [random.randint(0, size * 10) for _ in range(size)]
    print(f"Розмір масиву: {size}")
    print("Час виконання сортування злиттям:", timeit.timeit(
        lambda: merge_sort(arr.copy()), number=100))
    print("Час виконання сортування вставками:", timeit.timeit(
        lambda: insertion_sort(arr.copy()), number=100))
    print("Час виконання алгоритму Timsort:", timeit.timeit(
        lambda: sorted(arr.copy()), number=100))
    print()

# Зазвичай Timsort демонструє найкращу продуктивність на великих наборах даних,
# оскільки поєднує в собі переваги обох алгоритмів - сортування злиттям та сортування вставками.
# Таким чином, програмісти використовують вбудовані алгоритми сортування в Python,
# оскільки вони оптимізовані та забезпечують ефективну роботу навіть на великих обсягах даних.
