def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        # Calculate the position using the interpolation formula
        pos = low + ((high - low) // (arr[high] - arr[low])) * (target - arr[low])

        # Check if the target is found
        if arr[pos] == target:
            return pos
        # If the target is larger, it must be in the upper part
        elif arr[pos] < target:
            low = pos + 1
        # If the target is smaller, it must be in the lower part
        else:
            high = pos - 1

    return -1  # If the element is not found

# Get input from the user
arr = list(map(int, input("Enter a sorted array of integers (separated by spaces): ").split()))
target = int(input("Enter the target element to search for: "))

# Perform the search
result = interpolation_search(arr, target)

# Display the result
if result == -1:
    print("Element not found")
else:
    print(f"Element {target} found at index {result}")
