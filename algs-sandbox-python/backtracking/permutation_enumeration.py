


"""
Approach:
Choice of 3 letters at first step, 2 letters at second step, 1 letter at last step

"""
# remaining curr_permutation letter
# xyz   ""  "x" 
# yz  x   x
# y
#                   []
#       [x]         [y]             [z]
#    [xy]
#  [xyz]
#

def permutation_enumeration(arr):
    res = []
    def visit(partial_arr, remaining_chars):
        # base case, no remaining chars, otuput the partial arr
        if not remaining_chars:
            res.append(partial_arr.copy())
            return       ## MISSED THIS
        # make a choice 
        for choice in remaining_chars.copy():
            partial_arr.append(choice)
            remaining_chars.remove(choice)
            
            visit(partial_arr, remaining_chars)
            
            # back track, clean up 
            partial_arr.pop() 
            remaining_chars.add(choice)

    visit([], set(arr))
    return res


def permutation_enumeration(arr):
    res = []
    def visit(curr_permutation, letters_remaining):
        # nothing remaining 
        if not letters_remaining:
            res.append(curr_permutation.copy())
            return
        for choice in letters_remaining:
            new_choices = [c for c in letters_remaining if c != choice]
            curr_permutation.append(choice)
            visit(curr_permutation, new_choices)
            curr_permutation.pop() # backtrack
     
    visit([], arr)  
    return res


arr = ['x', 'y', 'z']
print(permutation_enumeration(arr))