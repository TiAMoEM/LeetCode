# -*- coding:utf-8 -*-

def binarySearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = left + 1
    return None