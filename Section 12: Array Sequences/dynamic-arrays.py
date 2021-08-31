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

    