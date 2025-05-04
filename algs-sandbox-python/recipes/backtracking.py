

"""
Four types of problem:
 - Feasibility: Is there a solution?
   "is there any non-empty subset that adds up to X"
 - Enumeration: List all the solutions
   "find all subsets that add up to X"
 - Counting: How many solutions are there ?
   "how many subsets add up to X?"
 - Optimistaion: Among all the solutions, which is the best?
   " which is the smallest subset that adds up to X?"

Pruning, skip a branch if we know it can't lead to a solution (i.e. sum over X for positive numbers)

Can often (but not always) be optimised with DP. Need Backtracking for enumeration versions of the problem.

5 design choices:
 1. Solution state to store solution in
 2. Child creation, do we need new data structures or traverse in state ?
 3. Pruning: Should we prune eagerly or lazily? Do we check boundaries before recursing or after?
 4. Leaf processing: What should we do with full solutions?
 5. Additional optimisation, anything else we can pass down the tree?
"""



def visit(partial_solution):
    if full_solution(partial_solution):
        # update solution state / process leaf 
        pass 
    else:
        for child in choices(partial_solution):
            # prune if applicable 
            child = apply_choice(partial_solution)
            visit(child)
    visit(empty_solution)