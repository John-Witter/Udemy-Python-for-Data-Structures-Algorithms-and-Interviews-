# Anagram Check

## Problem

Given two strings, check to see if they are anagrams.
An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

For example:

```python
        "public relations" is an anagram of "crap built on lies."

        "clint eastwood" is an anagram of "old west action"        
```

* Note: Ignore spaces and capitalization> So "d go" is an anagram of "God" and "dog" and "o d g".

# Solution

Fill out your solution below:

```python
def anagram(s1,s2):

    pass

anagram('dog', 'god') # OUTPUT: True
anagram('clint eastwood', 'old west action') # OUTPUT: True
anagram('aa', 'bb') # OUTPUT: False
```

# Test Your Solution
Run the cell below to test your solution:

```python
"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class AnagramTest(object):

    def test(self, sol):
        assert_equal(sol('go go go', 'ggooo'), True)
        assert_equal(sol('abc', 'cba'), True)
        assert_equal(sol('hi man', 'hi     man'), True)
        assert_equal(sol('aabbcc', 'aabbc'), False)
        print "ALL TEST CASES PASSED"

# Run tests
t = AnagramTest()
t.test(anagram) # OUTPUT: ALL TEST CASES PASSED
```