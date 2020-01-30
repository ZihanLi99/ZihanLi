class TargetNotFound(Exception):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return(repr(self.val))

def binarySearch(arr, searchItem):
    size = len(arr)
    beg = 0
    end = size - 1
    while(beg < end):
        mid = (beg + end) // 2
        if arr[mid] == searchItem:
            return mid
        elif arr[mid] > searchItem:
            end = mid - 1
        else:
            beg = mid + 1
    raise TargetNotFound("TargetNotFound")
