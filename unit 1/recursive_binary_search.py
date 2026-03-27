def binary_search(arr, key, low, high):
    # checking if element is present or not
    if low > high:
        return -1
    mid = int((low + high) / 2)   # finding middle
    if arr[mid] == key:
        return mid
    if key < arr[mid]:
        # go to left part
        return binary_search(arr, key, low, mid-1)
    else:
        # go to right part
        return binary_search(arr, key, mid+1, high)
# main
arr = [1,2,3,4,5,6]
print("Array is:", arr)
key = 4   # element to search
res = binary_search(arr, key, 0, len(arr)-1)
if res == -1:
    print("Not found")
else:
    print("Found at index", res)
