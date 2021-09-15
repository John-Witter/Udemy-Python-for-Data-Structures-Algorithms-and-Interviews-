def large_cont_sum(arr):
    
    # print()

    largest = 0
    currSum = 0

    # print('---------')

    for num in arr:
        currSum += num

        if num > currSum:
            # print('num > currSum:', num > currSum)
            currSum = num            

        # print('num', num, '\t\tcurrSum:', currSum, '\t\tlargest:', largest)

        if currSum >= largest:
            largest = currSum

    # print('---------')

    # print()
    return largest


print(large_cont_sum([1, 2, -1, 3, 4, 10, 10, -10, -1]))  # OUTPUT: 29

print(large_cont_sum([1, 2, -1, 3, 4, -1]))  # OUTPUT: 9

print(large_cont_sum([-1, 1]))  # OUTPUT: 1
