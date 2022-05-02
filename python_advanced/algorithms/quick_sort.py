"""Quick sort algorithm implementation"""

from collections import deque


def partition(unsorted_list, start, end):
    """
    Divides the list into a part in which the elements are
    greater than the pivot and a part in which there are less
    """
    pivot = unsorted_list[end]
    pivot_index = start

    for i in range(start, end):
        if unsorted_list[i] <= pivot:
            unsorted_list[i], unsorted_list[pivot_index] = \
                unsorted_list[pivot_index], unsorted_list[i]
            pivot_index = pivot_index + 1

    unsorted_list[end], unsorted_list[pivot_index] = unsorted_list[pivot_index], unsorted_list[end]

    return pivot_index


def quick_sort(unsorted_list):
    """Quick sort implementation"""
    stack = deque()

    start = 0
    end = len(unsorted_list) - 1

    stack.append((start, end))

    while stack:

        start, end = stack.pop()

        pivot_index = partition(unsorted_list, start, end)

        if pivot_index - 1 > start:
            stack.append((start, pivot_index - 1))

        if pivot_index + 1 < end:
            stack.append((pivot_index + 1, end))
