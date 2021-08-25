lst = [1,2,3]

# O(1) --> Constant Time
def func_constant(values):
    print(values[0])
# func_constant(lst) # OUTPUT: 1

# O(n) --> Linear Time
def func_linear(values):
    for val in values:
        print(val) # The number of print statements scales linearly with n
                   # For a list of 10 values, it prints 10 times

# func_linear(lst) # OUTPUT: 1\n2\n3

# O(n^2) Quadratic
def func_quadratic(values):
    for item_1 in lst: # for a list of n items
        for item_2 in lst: # perform n operations for every item in lst
            print(item_1, item_2) # a list of 9 values has 81 operations

# func_quadratic(lst) # OUTPUT: 1 1\n1 2\n1 3\n 2 1\n...\n3 1\n 3 2\n 3 3

# What is the Big O Time Complexity of comp?


def comp(lst):
    # print first value of lst
    print(lst[0]) # O(1)

    # print 1st 1/2 of list
    midpoint = int(len(lst) / 2)
    for val in lst[:midpoint]: # O(n/2)
        print(val)

    # print a string 10 times
    for x in range(10): # O(1)
        print('hello world')


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# comp(lst)
# O(1 + n/2 + 10) --> O(n)


# given a list, return a boolean indicating if a matched item is in the list
def matcher(lst, match):
    for item in lst:
        if item == match:
            return True
    return False


# print(matcher(lst, 1))  # True for lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(matcher(lst, 11))  # False for [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Best Case: match is first item in list --> O(1) --> Constant runtime

# Worst Case: no match, every item in list checked --> O(n) --> Linear



def create_list (n):
    new_list = []

    for num in range(n):
        new_list.append('new')
    
    return new_list


#print(create_list(5))  # OUTPUT: ['new', 'new', 'new', 'new', 'new']

# Time Complexity: O(n)
# Space Complexity: O(n)

###
# Quick note:
# Jose · Lecture 41 · 6 years ago
# Small error around the ~17 minute mark in lecture 41. The 'printer' function # should have used range(n) not range(10) in order to really be O(n) the 10 # was accidentally coded in .
#
# Thanks to Ian for pointing out the error! ###
def printer(n):
    
    for x in range(n):
        print('Hello World!')
    return ''

print(printer(10))

# Time Complexity: O(n)
# Space Complexity: O(1)