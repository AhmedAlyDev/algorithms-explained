def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_arr = []
    while arr:
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

# Example usage:
if __name__ == "__main__":
    print(selection_sort([5, 3, 6, 2, 10]))  # Output: [2, 3, 5, 6, 10]
