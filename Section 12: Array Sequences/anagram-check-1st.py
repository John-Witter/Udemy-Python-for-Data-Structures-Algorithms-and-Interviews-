def anagram(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    print(set1) # 
    print(set2) # 
    return set1 == set2

print(anagram('dog', 'god'))  # OUTPUT: True
print(anagram('clint eastwood', 'old west action'))  # OUTPUT: True
print(anagram('aa', 'bb'))  # OUTPUT: False

""" OUTPUT:
{'g', 'o', 'd'}
{'g', 'o', 'd'}
True
{'a', 'l', 'e', 'o', 'd', 't', 'i', 'c', 's', 'w', 'n', ' '}
{'a', 'o', 'l', 'd', 't', 'i', 'n', 'c', 's', 'w', 'e', ' '}
True
{'a'}
{'b'}
False
"""
