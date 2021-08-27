# Low Level Arrays

* A group of related variables stored one after another in a contiguous portion of computer memory
* Integer ***index*** is used to describe an element's location in memory
* Each cell of an array uses the same number of bytes
    * This allows O(1) access given an ***index***

</br>
</br>

# Referential Arrays
## Lists and Tuples are referential structures
* Imagine 100 student names w/ ID numbers
* Each cell of the array needs to have the same number of bytes
* How can we avoid having to have a series of names?
* We can use an array of object **References**
    * Each element is a **reference** to the object

</br>
</br>

## Referential Arrays 
* A single list instance may include multiple references to the same object as elemets of the list
* Single object may be an element of two or more lists
    * EX: slicing a list --> the result is a new list instance w/references to the same object
        * Reassigning values just changes where the list points to
        *  see: Referential Arrays.png

</br>
</br>

## Copying Arrays

```python
    primes = [1,3,5,7,11,13,17,19,23,27,29)
    backup = list(primes)
```
* This produces a new list that is a *****shallow copy***** in that it references the same elements as in the first list
* If the contents of the list were of a mutable type, a *****deep copy*****, meaning a new list with new elements, can be produced by using the deepcopy function from the copy module

```python
    counters = [0] * 8 # all cells reference the same object (integers are immutable)
    
    counters[2] += 1 # counters[2] will reference the newly computed value, not the original 0
```

