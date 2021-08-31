import ctypes # "a raw array holder" used when we make a new array
import sys # getsizeof()

class DynamicArray(object):
    '''
    DYNAMIC ARRAY CLASS (Similar to Python List)
    '''

    def __init__(self):
        self.n = 0 # Count actual elements (Default is 0)
        self.capacity = 1 # Default Capacity
        self.A = self.make_array(self.capacity)

    def __len__(self):
        """
        Return number of elements stored in array
        """
        return self.n
    
    def __getitem__(self,k):
        """
        Return element at index k
        """
        if not 0 <= k < self.n: # if k isn't b/t 0 and count 
            return IndexError('K is out of bounds!')

        return self.A[k] # return the array at index k

    def append (self, ele): # add an element to the end of the array
        if self.n == self.capacity: # check capacity
            self._resize(2*self.capacity) # _ before method makes it non-public
        self.A[self.n] = ele
        self.n += 1

    def _resize (self, new_cap): 
        B = self.make_array(new_cap)

        for k in range(self.n):
            B[k] = self.A[k] # make B = A
        self.A = B # reassign A to B
        self.capacity = new_cap # reset capacity

    def make_array(self, new_cap): # return a new array w/a new capacity
        return (new_cap * ctypes.py_object)()


####### TEST  class DynamicArray(object)  #####

arr = DynamicArray()
arr.append(1)
print(len(arr)) # 1
print('sys.getsizeof(arr)): ', sys.getsizeof(arr))

arr.append(2)
print(len(arr)) # 2
print('sys.getsizeof(arr)): ', sys.getsizeof(arr))

print(arr[0]) # 1
print(arr[1]) # 2

arr2 = DynamicArray()
for i in range(500):
    # Numer of elements in data
    a = len(arr2)

    # Actual size in Bytes
    b = sys.getsizeof(arr2)

    print('Length: {0:3d}; Size in bytes: {1:4d}; i: {2} '.format(a, b, i))
    
    arr2.append(i)
