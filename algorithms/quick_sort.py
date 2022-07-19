import random


def quick_sort(arr: list):
    if len(arr) < 2:
        return arr
    pivot_index = random.randrange(len(arr))
    pivot_val = arr.pop(pivot_index)

    lower = [i for i in arr if i <= pivot_val]
    greater = [x for x in arr if x > pivot_val]

    return quick_sort(lower) + [pivot_val] + quick_sort(greater)
