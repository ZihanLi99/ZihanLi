class TargetNotFoundException(Exception):
    pass

def bin_except(arr,target):
    low = 0
    high = len(arr)-1
    found = False
    index =- 1
    while( low<=high and not found):
        mid = (low + high)//2 
        if arr[mid] == target: 
            found=True
            index=mid
        else:
            if target < arr[mid]: 
                high = mid - 1
            else: 
                low = mid + 1
    try:
        if not found:
            raise TargetNotFoundException
        else:
            print("Target is Found at index: ",index)
    except TargetNotFoundException:
         print("Target Is Not Found in array ")
