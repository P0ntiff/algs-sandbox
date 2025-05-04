# # Aligned Chain

# Given a binary tree, we say a node is aligned if its value is equal to its depth (distance from root). Return the length of the longest descendant chain of aligned nodes. The chain does not need to start at the root.

# ```
# Example:
#                 7
#                / \
#               1   3
#              / \   \
#             2   8   2
#            / \     / \
#           4   3   3   3

# Output: 3. The longest chain of aligned nodes is 1 -> 2 -> 3 on the left subtree.
# ```

class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key 
        self.left: TreeNode = left
        self.right: TreeNode = right

#                 7
#                / \
#               1*   3
#              / \   \
#             7*   8   2
#            / \     / \
#           4   3*   3   3


def longest_chain(root: TreeNode):
    max_chain = 0
    def chain_length(node: TreeNode, depth: int = 0):
        nonlocal max_chain
        if node is None:
            return 0

        left_length = chain_length(node.left, depth + 1)
        right_length = chain_length(node.right, depth + 1) # 1

        curr_chain = 0
        if node.key == depth:
            curr_chain = max(left_length, right_length) + 1
            max_chain = max(max_chain, curr_chain)
        return curr_chain
    chain_length(root, 0)
    return max_chain

import unittest 

class ChainTests(unittest.TestCase):
    def test_depth_zero_case(self):
        t = TreeNode(0)
        self.assertEqual(longest_chain(t), 1)
    
    def test_example_tree(self):
        # Example tree from the problem description
        #                 7
        #                / \
        #               1   3
        #              / \   \
        #             2   8   2
        #            / \     / \
        #           4   3   3   3
        t = TreeNode(7, TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(8)), TreeNode(3, TreeNode(2, TreeNode(3), TreeNode(3))))
        self.assertEqual(longest_chain(t), 3)


unittest.main(exit=False)