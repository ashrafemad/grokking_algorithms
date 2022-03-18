

def binary_search(sorted_list: list, element_to_find):
    low = 0
    high = len(sorted_list) - 1  # last index of the list

    while low <= high:
        mid = (low + high) // 2  # get the middle index of list
        guess = sorted_list[mid]
        if guess == element_to_find:
            return mid
        if guess > element_to_find:
            high = mid - 1
        if guess < element_to_find:
            low = mid + 1
    return None
