```python
def sum1(n):
    final_sum = 0

    for x in range(n+1): # iteratively add to final_sum
        final_sum += x
    
    return final_sum

print('sum1()')
print(sum1(10))
print(sum1(5))
print(sum1(2))


def sum2(n): # uses *** 
    return (n*(n+1)) / 2


print('\nsum2()')
print(sum2(10))
print(sum2(5))
print(sum2(2))

```

* *** sum2 uses the following summation: </br></br>
## $\sum_{i=0}^{n}i = \frac{n(n+1)}{2}$ 
