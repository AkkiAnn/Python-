def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Current element is smallest
        min_index = i
        for j in range(i + 1, n):
            # Compare lexicographically
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap smallest element with first element of unsorted portion
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
# Test function
arr = ["Steve", "Alice", "bob", "Charlie", "dave"]
sorted_arr = selection_sort(arr)
print(sorted_arr)
