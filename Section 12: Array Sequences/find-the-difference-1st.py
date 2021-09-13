def finder(arr1, arr2):

    d1 = {}
    d2 = {}

    for num in arr1:
        if num in d1:
            d1[num] += 1
        else:
            d1[num] = 1

    for num in arr2:
        if num in d2:
            d2[num] += 1
        else:
            d2[num] = 1
    
    print(d1)
    print(d2)

    for key in d1:
        if key not in d2 or d2[key] != d1[key]:
            return key


arr1 = [1, 2, 3, 4, 5, 6, 7]
arr2 = [3, 7, 2, 1, 4, 6]
print(finder(arr1, arr2))  # OUTPUT: 5

arr1 = [5, 5, 7, 7]
arr2 = [5, 7, 7]
print(finder(arr1, arr2))  # OUTPUT: 5
