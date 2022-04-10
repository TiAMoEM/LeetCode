"""
def partition(arr, left, right):
    pivotkey = arr[left]
    while left < right:
        while left < right and arr[right] >= pivotkey:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= pivotkey:
            left += 1
        arr[right] = arr[left]

    arr[left] = pivotkey
    return left

def q_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        q_sort(arr, left, pivot-1)
        q_sort(arr, pivot+1, right)
    return arr

def quick_sort(arr):
    return q_sort(arr, 0, len(arr) - 1)

"""


def quickSort(arr, left, right):
    if left < right:
        pivot = arr[left]
        low = left
        high = right
        while left < right:
            while left < right and arr[right] >= pivot:
                right -= 1
            arr[left] = arr[right]
            while left < right and arr[left] <= pivot:
                left += 1
            arr[right] = arr[left]

        arr[left] = pivot
        quickSort(arr, low, left - 1)
        quickSort(arr, left + 1, high)
    return arr
