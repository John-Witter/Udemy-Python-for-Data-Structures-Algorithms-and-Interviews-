# Quiz 1: Algorithm and Big O Quiz

## Question 1

Give the Big-O performance (performance is time complexity) of the following code:

```python
    for x in range(n):
        for y in range(n):
            print 'hi!'
```

1. O(n)
1. O(log(n))
1. O($n^2$)
1. O(1)
1. None of the above

### Answer:
* 3. O($n^2$)

</br>
</br>

## Question 2

Give the Big-O performance (performance is time complexity) of the following code:

```python
    for val in range(n):
        print('done')
```

1. O(n)
1. O(1)
1. O(log(n))
1. O($n^3$)
1. None of the above

### Answer:
* 1. O(n)

</br>
</br>

## Question 3

Give the Big-O performance (performance is time complexity) of the following code:

```python
    x = n
    while x > 0:
        y = 2 + 2
        x = x // 2 # // is int division. ex: 10//3 = 3 ex: 10/3 = 3.333...
```

1. O(log(n))
1. O(n)
1. O(1)
1. O($n^2$)
1. None of the above

### Answer:
* 1. O(log(n))
* ``` n ``` is halved each iteration

</br>
</br>

## Question 4

Give the Big-O performance (performance is time complexity) of the following code:

```python
    w = 0
    for x in range(n):
        w = w + 1

    for y in range(n):
        w = w - 1
```

1. O(n)
1. O($n^2$)
1. O(log(n))
1. O(3n)
1. O(1)
1. None of the above

### Answer:
* 1. O(n)

</br>
</br>

## Question 5

Give the Big-O performance (performance is time complexity) of the following code:

```python
for x in range(n):
    z = 2 + 2
for y in range(n):
    z = 2 + 2
for w in range(n):
    z = 2 + 2
```

1. O(n)
1. O(3)
1. O(log(n))
1. O($n^3$)
1. None of the above

### Answer:
* 1. O(n)