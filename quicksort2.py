def quicksort(List, low, high):
    if low >= high:
        return List
    else:
        flag = List[low]
        left = low
        right = high
        while left < right:
            while left < right and List[right] >= flag:
                right -= 1
            List[left] = List[right]
            while left < right and List[left] <= flag:
                left += 1
            List[right] = List[left]
        List[right] = flag
        quicksort(List, low, left-1)
        quicksort(List, left+1, right)
        return List
