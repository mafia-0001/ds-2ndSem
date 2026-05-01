def binary_search(arr, low, high, key):
    if low > high:
        return -1
    mid = (low + high)//2
    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, low, mid-1, key)
    else:
        return binary_search(arr, mid+1, high, key)

arr = [1,2,3,4,5,6]
print(binary_search(arr,0,len(arr)-1,4))