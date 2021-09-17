"""
Create a dictionary from arr1 and arr2 in the form of { key=num: val=numCount }
For nums in arr2, if arr1[num] not equal to arr2[num], then return that num
"""

def finder(arr1, arr2):
    arr1Dict = {}
    arr2Dict = {}
        
    for num in arr1:
        if num in arr1Dict:
            arr1Dict[num] += 1
        else:
            arr1Dict[num] = 1
        
    for num in arr2:
        if num in arr2Dict:
            arr2Dict[num] += 1
        else:
            arr2Dict[num] = 1

    for num in arr1Dict:
        if not num in arr2Dict or arr1Dict[num] != arr2Dict[num]:
            return num

    return None


arr1 = [1, 2, 3, 4, 5, 6, 7]
arr2 = [3, 7, 2, 1, 4, 6]
print(finder(arr1, arr2))  # OUTPUT: 5

arr1 = [5, 5, 7, 7]
arr2 = [5, 7, 7]
print(finder(arr1, arr2))  # OUTPUT: 5

arr1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
arr2 = [9, 8, 7, 5, 4, 3, 2, 1]
print(finder(arr1, arr2))  # OUTPUT: 6


