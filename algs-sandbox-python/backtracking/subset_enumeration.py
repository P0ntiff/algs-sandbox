"""
Given a set S, return all possible subsets in any order


"""

def generate_subsets_bugged(S):
    output = []
    output.append([]) # empty set is always a valid subset
    # backtracking soluion: DFS down the decision tree
    # branch factor: up to 2 choices to include or exclude a letter
    # depth: number of letters
    #                  []
    #           [x]             []
    #   [xz]        [x]       [z]     []
    # [xzy] [xz] [xy]  [x]  [zy] [z] [y] []
    available_letters = S
    def visit(letters_left, curr_letter, curr_subset, depth):
        # check for end solution
        if len(letters_left) == 0 or depth == len(S):
            # leaf node
            output.append(curr_subset.copy())
            return
        # update partial solution
        if curr_letter != "":
            curr_subset.append(curr_letter)
        else:
            # call for each child
            next_choice = letters_left.pop()
            visit(letters_left, next_choice, curr_subset, depth + 1)
            letters_left.append(next_choice)
            visit(letters_left, "", curr_subset, depth + 1)
    visit(S.copy(), "", [].copy(), 0)
    return output

def generate_subsets(S):
    res = []    # Global list of subsets
    subset = [] # partial solution
    def visit(i): 
        # leaf node 
        if i == len(S):
            res.append(subset.copy())   # copy s
            return 
        # for each choice , visit
        # choice 1: pick this letter  (include)
        subset.append(S[i])
        visit(i + 1)
        # choice 2: don't pick this letter (exclude)
        subset.pop() # cleanup choice 1
        visit(i + 1)
    visit(0)
    return res 

S = ['x', 'y', 'z']

expected_output = [[], ['x'], ['y'], ['z'], ['x', 'y'], ['x', 'z'], ['y', 'z'], ['x', 'y', 'z']]
print(generate_subsets(S))
