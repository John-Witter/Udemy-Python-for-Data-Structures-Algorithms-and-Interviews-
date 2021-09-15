def large_cont_sum(arr):

    # Check to see if array is length 0
    if len(arr) == 0:
        return 0

    # Start the max and current sum at the first element
    max_sum = current_sum = arr[0]

    # For every element in array skipping arr[0]
    for num in arr[1:]:

        # Set current sum as the higher of the two
        current_sum = max(current_sum + num, num)

        # Set max as the higher between the current_sum and max_sum
        max_sum = max(current_sum, max_sum)

    return max_sum


print(large_cont_sum([1, 2, -1, 3, 4, 10, 10, -10, -1]))  # OUTPUT: 29

print(large_cont_sum([1, 2, -1, 3, 4, -1]))  # OUTPUT: 9

print(large_cont_sum([-1, 1]))  # OUTPUT: 1
