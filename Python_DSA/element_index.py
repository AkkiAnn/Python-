def find_element(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
# Test function
arr = [1, 2, 3, 4]
x = 3
print(find_element(arr, x))
