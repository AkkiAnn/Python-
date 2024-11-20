def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n  # Initialize result array with -1
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                result[i] = arr[j]
                break
    return result
# Test function
arr = [4, 5, 2, 25]
result = next_greater_element(arr)
for i in range(len(arr)):
    print(f"{arr[i]} -> {result[i]}")
