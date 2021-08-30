# Dynamic Arrays
* Size is mutable
* Lists in Python

```python
import sys # getsizeof() --> returns size in bytes
# Set n 
n = 50

data = []

for i in range(n):

    # Numer of elements in data
    a = len(data)

    # Actual size in Bytes
    b = sys.getsizeof(data)

    print('Length: {0:3d}; Size in bytes: {1:4d} '.format(a,b))

    # increase length by one
    data.append(n)
```

* Length:   0; Size in bytes:   56 
* Length:   1; Size in bytes:   88 
* Length:   2; Size in bytes:   88 
* Length:   3; Size in bytes:   88 
* Length:   4; Size in bytes:   88 
* Length:   5; Size in bytes:  120 
* Length:   6; Size in bytes:  120 
* Length:   7; Size in bytes:  120 
* Length:   8; Size in bytes:  120 
* Length:   9; Size in bytes:  184 
* Length:  10; Size in bytes:  184 
* Length:  11; Size in bytes:  184 
* Length:  12; Size in bytes:  184 
* Length:  13; Size in bytes:  184 
* Length:  14; Size in bytes:  184 
* Length:  15; Size in bytes:  184 
* Length:  16; Size in bytes:  184 
* Length:  17; Size in bytes:  248 
* Length:  18; Size in bytes:  248 
* Length:  19; Size in bytes:  248 
* Length:  20; Size in bytes:  248 
* Length:  21; Size in bytes:  248 
* Length:  22; Size in bytes:  248 
* Length:  23; Size in bytes:  248 
* Length:  24; Size in bytes:  248 
* Length:  25; Size in bytes:  312 
* Length:  26; Size in bytes:  312 
* Length:  27; Size in bytes:  312 
* Length:  28; Size in bytes:  312 
* Length:  29; Size in bytes:  312 
* Length:  30; Size in bytes:  312 
* Length:  31; Size in bytes:  312 
* Length:  32; Size in bytes:  312 
* Length:  33; Size in bytes:  376 
* Length:  34; Size in bytes:  376 
* Length:  35; Size in bytes:  376 
* Length:  36; Size in bytes:  376 
* Length:  37; Size in bytes:  376 
* Length:  38; Size in bytes:  376 
* Length:  39; Size in bytes:  376 
* Length:  40; Size in bytes:  376 
* Length:  41; Size in bytes:  472 
* Length:  42; Size in bytes:  472 
* Length:  43; Size in bytes:  472 
* Length:  44; Size in bytes:  472 
* Length:  45; Size in bytes:  472 
* Length:  46; Size in bytes:  472 
* Length:  47; Size in bytes:  472 
* Length:  48; Size in bytes:  472 
* Length:  49; Size in bytes:  472 

<hr>
</br>
</br>
</br>
<hr>

# Dynamic Array Implementation
* The key is to provide means to grow the array ***`A`*** that stores the elements of a list
* We can't actually grow that array, its capacity is fixed.

1. Allocate a new array B with larger capacity
2. Set ***`B[i] = A[i]`*** for ***`i = 0,...,n-1`***, where ***`n`*** denotes current number of items
3. Set ***`A = B`***
4. Insert the new element in the new array
    * Typically ***`B`*** will have twice the capacity of ***`A`***
