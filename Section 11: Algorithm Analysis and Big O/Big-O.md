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