__author__ = 'FSG'
def quicksort(arr, low, high):
    if len(arr) <= 1:
        return
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)

def partition(arr, low, high):
    tmp = arr[low]
    while low < high:
        while low < high and arr[high] >= tmp:
            high -= 1

        if low < high:
            arr[low] = arr[high]

        while low < high and arr[low] <= tmp:
            low += 1

        if low < high:
            arr[high] = arr[low]

    arr[low] = tmp
    return low

mylist = [11, 10, 3, 12, 33, 1000, 1, 333, -11]
quicksort(mylist, 0, len(mylist) - 1)
print(mylist)