def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return None

# Example usage:
if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9]
    print(binary_search(numbers, 3))  # Output: 1
    print(binary_search(numbers, -1))  # Output: None
