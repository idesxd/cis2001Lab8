def merge_sort(numbers):
    """Sort a list using merge sort and return a new sorted list."""

    if len(numbers) <= 1:
        return numbers

    midpoint = len(numbers) // 2
    left_half = merge_sort(numbers[:midpoint])
    right_half = merge_sort(numbers[midpoint:])

    return merge_lists(left_half, right_half)


def merge_lists(left_list, right_list):
    """Merge two sorted lists into one sorted list."""

    merged_list = []
    left_position = 0
    right_position = 0

    while left_position < len(left_list) and right_position < len(right_list):

        if left_list[left_position] <= right_list[right_position]:
            merged_list.append(left_list[left_position])
            left_position += 1
        else:
            merged_list.append(right_list[right_position])
            right_position += 1

    merged_list.extend(left_list[left_position:])
    merged_list.extend(right_list[right_position:])

    return merged_list


user_input = input("Enter numbers separated by spaces: ")

numbers = [int(value) for value in user_input.split()]

sorted_numbers = merge_sort(numbers)

print("Sorted numbers:", sorted_numbers)