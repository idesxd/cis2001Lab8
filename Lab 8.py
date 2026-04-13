def merge_sort(arr):
    """Sort a list using merge sort and return a new sorted list."""
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left_half = merge_sort(arr[:middle])
    right_half = merge_sort(arr[middle:])

    return merge(left_half, right_half)


def merge(left, right):
    """Merge two sorted lists into one sorted list."""
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


user_input = input("Enter numbers separated by spaces: ")

numbers = [int(x) for x in user_input.split()]

sorted_numbers = merge_sort(numbers)

print("Sorted numbers:", sorted_numbers)