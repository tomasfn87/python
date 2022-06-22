def binary_search(arr, term, start, end):
    mid = (start + end) // 2

    if end < start:
        return False

    if term == arr[mid]:
        return mid

    if term < arr[mid]:
        return binary_search(arr, term, start, mid-1)

    if term > arr[mid]:
        return binary_search(arr, term, mid+1, end)