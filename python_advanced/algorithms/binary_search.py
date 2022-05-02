"""Binary search method"""


def binary_search(elem_list, value):
    """Binary search method"""
    elem_list.sort()
    start = 0
    end = len(elem_list)

    while start <= end:
        middle = (start + end) // 2
        if elem_list[middle] == value:
            return middle
        if elem_list[middle] > value:
            end = middle - 1
        else:
            start = middle + 1

    return "No such element!"
