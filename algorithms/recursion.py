

def sum_using_recursion(arr):
    if not arr:
        return 0
    return arr[0] + sum_using_recursion(arr[1:])
