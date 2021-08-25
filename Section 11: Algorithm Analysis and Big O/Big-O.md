# Big O Notation

## Common Runtimes

| Big-O | Name |
| :---- | :----|
| 1 | Constant |
| log(n) | Logarithmic |
| n | Linear |
| nlog(n) | Log Linear |
| $n^2$| Quadratic |
| $n^3$| Cubic |
| $2^n$| Exponential |


```python
def sum1(n):
    final_sum = 0
    for x in range(n+1): # O(n) --> Linear Time
        final_sum += x    
    return final_sum

def sum2(n): # O(1) --> Constant Time
    return (n*(n+1)) / 2
```
</br>
</br>

## Drop constants
* Significant 

```python
# What is the Big O Time Complexity print_2?
def print_2(lst):
    for val in lst:
        print(val)
    for val in lst:
        print(val)
```
* **O(n)**
* 2 for loops each is O(n) --> O(2n) --> DROP CONSTANTS --> O(n)

</br>

```python
# What is the Big O Time Complexity of comp?
def comp(lst):
    # print first value of lst
    print(lst[0])

    # print 1st 1/2 of list
    midpoint = len(lst) / 2
    for val in lst[:midpoint]:
        print(val)

    # print a string 10 times
    for x in range(10):
        print('hello world')

lst = [1,2,3,4,5]
comp(lst)
````