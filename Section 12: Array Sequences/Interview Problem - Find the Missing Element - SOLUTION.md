# Find the Missing Element

## Problem
Consider an array of non-negative integers. A second array is formed by shuffling
the elements of the first array and deleting a random element. Given these two
arrays, find which element is missing in the second array.

Here is an example input, the first array is shuffled and the number 5 is 
removed to construct the second array.

Input:

```python
    finder([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])
```

Output:

```python
    '5 is the missing number'
```

## Solution

The naive solution is go through every elemetn in the second array and check
whether it appears in the first array. Note that there may be duplicate
elements in the arrays so we should pay special attention to it. 
The complexity of this approach is O(N<sup>2</sup>), since we would need 
two for loops.

A more efficient solution is to sort the first array, so while checking whether
an element in the first array appears in the second, we can do a binary search
(we'll learn about binary search in more detail in a future section).
But we should still be careful about duplicate elements. The complexity is O(NlogN).

If we don't want to deal with the special case of duplicate numbers, we can sort
both arrays and iterate over them simultaneously. Once two iterators have
different values we can stop. The value of the first iterator is the missing
element. This solution is also O(NlogN). Here is the solution for this approach:

```python
def finder(arr1, arr2):
    
    # Sort the arrays
    arr1.sort()
    arr2.sort()

    # Compare the arrays
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
    
    return arr1[-1]

arr1 = [1, 2, 3, 4, 5, 6, 7]
arr2 = [3, 7, 2, 1, 4, 6]
finder(arr1, arr2) # OUTPUT: 5

arr1 = [5, 5, 7, 7]
arr2 = [5, 7, 7]
finder(arr1, arr2) # OUTPUT: 5    
```

## ```zip``` 

```python
print(zip([1, 2, 3], [4, 5, 6])) 
# OUTPUT: [(1, 4), (2, 5), (3, 6)]
``` 

## Solution using hash tables

```python
import collections

# Default dict from collections modual
    # a regular python dict, where if the key isn't in the dict
    # it will auto add it
    # easy way to avoid key errors

def finder2(arr1, arr2):

    d = collections.defaultdict(int)

    # add a count for every element in arr2
    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num

        else:
            d[num] -= 1

arr1 = [5, 5, 7, 7]            
arr2 = [5, 7, 7]            
print(finder2(arr1, arr2)) # OUTPUT: 5
```


## Solution using addition and subtraction

* Find the sum of arr1 and arr2
* arr1Sum - arr2Sum = solution
    * could be a stack overflow problem
    * might lose data if nums are long decimals
    * not best approach


## Linear time and space Solution

*   Initialize a var to 0
*   XOR every element in arr1 and arr2 with the var

```python
def finder3(arr1, arr2):
    res = 0

    # Perform an XOR b/t the nums in the arrays
    for num in arr1+arr2:
        res ^= num
        print res

    return res
```

## [XOR](https://en.wikipedia.org/wiki/Exclusive_or#:~:text=Exclusive%20or%20or%20exclusive%20disjunction,%2C%20the%20other%20is%20false.&text=The%20negation%20of%20XOR%20is,two%20inputs%20are%20the%20same.)

