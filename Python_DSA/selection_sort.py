def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Index of smallest element in unsorted portion
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap smallest element with first element in unsorted portion
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
# Test function
arr = [14, 46, 43, 27, 57, 41, 45, 21, 70]
sorted_arr = selection_sort(arr)
print(sorted_arr)
