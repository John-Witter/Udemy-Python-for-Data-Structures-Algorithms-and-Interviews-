# Anagram Check Solution

If each letter shows up the same number of times in both strings, 
    then they are anagrams.

If two sorted strings are equal to each other, then they are anagrams.


```python
def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower() # remove spaces and make lowercase
    s2 = s2.replace(' ', '').lower() # remove spaces and make lowercase

    return sorted(s1) == sorted(s2) # sorted is not optimal

anagram('god', 'dog') # OUTPUT: True
anagram('clint eastwood', 'old west action') # OUTPUT: True
anagram('clint eastwood', 'olsd west action') # OUTPUT: False

```
</br>
</br>

Solution using counting and Python dictionaries:

```python
def anagram2(s1, s2):
    
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Edge Case Check
    # Strings must have same number of letters
    if len(s1) != len(s2): 
        return false
    
    # Create a counting dictionary
    count = {} # count frequency of each letter appearance 
                 # check that all counts are equal
    
    # Add counts for s1
    # Subtract counts for s2
    # Anagrams = 0

    # add letters in s1 to count and count them
    for letter in s1:
        # if letter in dictionary
        if letter in count:
            count[letter] += 1 # add 1 to letter key
        else: 
            count[letter] = 1 # else, letter = 1

    # subtract each letter in s2 from count if it exists in count
    # else, add letter to count with value 1
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    # check that all counts are 0
    for k in count:
        if count[k] != 0:
            return False
    
    # they are anagrams
    return True

anagram('god', 'dog') # OUTPUT: True
anagram('clint eastwood', 'old west action') # OUTPUT: True
anagram('clint eastwood', 'olsd west action') # OUTPUT: False    
```

</br>
</br>
</br>

# Steps

1. Clean up input strings
    * Remove whitespace
    * Turn letters lowercase

2. Edge Case Check
    * Return false if strings have different length

3. Create a dictionary: ```count```

4. For every letter in the first string
    * If letter is in ```count```, ```count[letter] += 1```
    * Else, ```count[letter] = 1```

5. For every letter in the second string    
    * If letter is in ```count```, ```count[letter] -=1```
    * Else, ```count[letter] = 1```

6. For every letter in ```count```
    * If ```count[letter] !=0```, ```return False```

7. Return True    