

# Approach: Backtracking to enumerate all string permutations
# Start with a character, branch out choosing a character in its next character set 
# Generate the string and print as we go. Stop when we get to length n
# Print in increasing length order
# Time: O(m^n) where m is the depth is at most n, branching factor m is the maximum length of the next character entry lists, which may be constant but we still have exponential time in terms of n , 
# Space: O(m) at m recursive calls maximum depth of the call stack. We aren't storing the result so we save there
def generate_valid_strings(starting_characters, next_character_map, n):
    def visit(char_array):
        # print this string 
        print("".join(char_array))

        # base case, hit length n
        if len(char_array) == n:
            return 
       
        # for each character in next character map entry
        for choice in next_character_map[char_array[-1]]:
            # increase length and visit TODO: optimise, string concatenate generates a copy
            char_array.append(choice)
            visit(char_array)
            char_array.pop()
        
    for start in starting_characters:
        visit(list(start))

print(generate_valid_strings(['a', 'b', 'c'], {
    'a': ['b' , 'c'],
    'b': ['a'],
    'c': ['a', 'b']
}, 4))
"""

Example 1:

starting_characters = ['a', 'b', 'c']
next_character_map = {
    'a': ['b' , 'c'],
    'b': ['a'],
    'c': ['a', 'b']
}
n = 4

Expected output:

'a'
'b'
'c'
'ab'
'ac'
'ba'
'ca'
'cb'
'aba'
'aca'
'acb'
...

Problem for today:

Write a program to generate all "valid strings" up to a certain length. A valid
string is a string that starts with an "allowed starting character", and in
which every character is followed by an "allowed" character. You are given a
list of starting allowed characters and a dictionary mapping each character to
a list of allowed characters that can follow it in valid strings. You are also
given an integer n > 0 and you should generate all valid strings up to and
including length n.

Print the output to console directly. You do not need to store all the output
in a list or other collection.

Example 1:

starting_characters = ['a', 'b', 'c']
next_character_map = {
    'a': ['b' , 'c'],
    'b': ['a'],
    'c': ['a', 'b']
}
n = 4

Expected output:

'a'
'b'
'c'
'ab'
'ac'
'ba'
'ca'
'cb'
'aba'
'aca'
'acb'
...

...
'caca'
...
'cbac'

Example 2:

starting_characters = ['a']
next_character_map = {
    'a': ['b'],
    'b': ['a'],
}
n = 4

Expected output:

'a'
'ab'
'aba'
'abab'

Example 3:
starting_characters = ['a']
next_character_map = {
    'a': [],
    'b': ['a'],
}
n = 40

Expected output:

'a'


"""