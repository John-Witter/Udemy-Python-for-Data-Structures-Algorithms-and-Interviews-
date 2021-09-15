def rev_word(s):
    revS = s.split() # create a list from the s string
 
    revS = revS[::-1] # reverse the list

    return ' '.join(revS) # return the list as a string with a space b/t words

print(rev_word('Hi John,   are you ready to go?'))
# OUTPUT: 'go? to ready you are John, Hi'

print(rev_word('    space before'))
# OUTPUT: 'before space'

print(rev_word('space after   '))
# OUTPUT: 'after space'

print(rev_word('   Hello John   how are you   '))
# OUTPUT: 'you are how John Hello'
