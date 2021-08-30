# Amortization

## Amortized Analysis of Dynamic Arrays
* The strategy of replacing an array with a new, larger array might at first seem slow
* A single append() opperation may require O(n) time to perform
* Our new array allows us to add ***n*** new elements beforee the array must be replaced again

1. Allocate memory for a larger array of size, typically twice the old array
2. Copy the contents of old array to new array
3. Free the old array