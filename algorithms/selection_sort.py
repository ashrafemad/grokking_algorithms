

def get_min_element_index(arr):
    '''
    will return the minimum index of an array
    by iterating over the array and recording the min value found
    :param arr:
    :return: minimum value index of type int
    '''
    min_val_index = 0
    for i in range(0, len(arr)):
        if arr[i] < arr[min_val_index]:
            min_val_index = i
    return min_val_index


def selection_sort(arg):
    '''
    :param arg: of type list
    :return: None if arg is empty list or not a list
    :return: ordered list of type list
    '''
    if not arg or type(arg) != list:
        return None
    new_ordered_list = []
    for element in range(0, len(arg)):
        min_value_index = get_min_element_index(arg)
        new_ordered_list.append(arg.pop(min_value_index))
    return new_ordered_list
