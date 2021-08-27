# Big O for Python Data Structures

## Lists
* Lists act as dynamic arrays
* O(1) - Indexing and assigning to an index postion

```python
    def method1():
        l = []
        for n in range(10000):
            l = l + [n]

    def method2():
        l = []
        for n in range(10000):
            l.append(n)
    
    def method3():
        l = [n for n in range(10000)] # list comprehension
    
    def method4():
        l = list(range(1000))

```

### Big-O for common list operations

| Operation | Big-O Efficiency |
| :--- | :--- |
| index [] | O(1) | 
| index assignment | O(1) |
| append | O(1) |
| pop() | O(1) |
| pop(i) | O(n) |
| insert(i, item) | O(n) |
| del operator | O(n) |
| iteration | O(n) |
| contains(in) | O(n) |
| get slice [x:y] | O(k) |
| del slice | O(n) |
| set slice | O(n + k) |
| reverse | O(n) |
| concatenate | O(k) |
| sort | O(nlogn) |
| multiply | O(nk) |

</br>
</br>

## Dictionaries
* Dictionaries are an implementaion of a hash table
* They operate with key value pairs
* O(1) Getting and Setting items

ex:
```python
    d = {'k1':1, 'k2':2} # d['k1'] = 1
```

| Operation | Big-O Efficiency |
| :--- | :--- |
| copy | O(n) | 
| get item | O(1) | 
| set item | O(1) | 
| delete item | O(1) | 
| contains(in) | O(1) | 
| iteration | O(n) | 