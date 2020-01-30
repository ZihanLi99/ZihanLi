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

arr = []
print("Enter the numbers -1 to stop")
while(True):
    num = int(input(""))
    if num == -1:
        break
    arr.append(num)
arr.sort()
print("After sorting your list is : ", arr)
searchItem = int(input("Enter the number to search:"))
try:
    ind = binarySearch(arr, searchItem)
    print("Your number is found in the list at the index {}".format(ind))
except TargetNotFound as error:
    print(error.val)
