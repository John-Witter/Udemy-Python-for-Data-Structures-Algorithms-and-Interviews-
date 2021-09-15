# [Largest Continuous Sum](https://www.udemy.com/course/python-for-data-structures-algorithms-and-interviews/learn/lecture/4088590#questions)

## Problem
Given an array of integers (positive and negative) find the largest continuous sum.

## Solution
If the array is all positive, then the result is simply the sum of all numbers.
The negative numbers in the array will cause us to need to begin checking sequences.

The algorithm is, we start summing up the numbers and store in a current sum variable.
After adding each element, we check whether the current sum is larger than the 
maximum sum so far. If it is, we update the maximum sum. As long as the current
sum is positive, we keep adding the numbers. When the current sum becomes negative,
we start with a new current sum. Because the negative sum will only decrease the 
sum of a future sequence. Note that we don't reset the current sum to 0 becuase
the array can contain all negative integers. Then the result would be the largest 
negative number.

```python
def large_cont_sum(arr):

    # Check to see if array is length 0
    if len(arr) == 0:
        return 0

    # Start the max and current sum at the first element
    max_sum = current_sum = arr[0]

    # For every element in array
    for num in arr[1:]:

        # Set current sum as the higher of the two
        current_sum = max(current_sum + num, num)

        # Set max as the higher between the current_sum and max_sum
        max_sum = max(current_sum, max_sum)

    return max_sum
```