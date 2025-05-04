from collections import deque

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        """Inserts a new node with the given key into the BST."""
        self.root = self.insert_recursive(self.root, key)

    def insert_recursive(self, node: TreeNode, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self.insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self.insert_recursive(node.right, key)
        return node
        
    def search(self, key):
        """Searches for a node with the given key.
        Returns the node if found, otherwise returns None.
        """
        return self.search_recursive(self.root, key)

    def search_recursive(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return node 
        if key < node.key:
            return self.search_recursive(node.left, key)
        else:
            return self.search_recursive(node.right, key)

    def delete(self, key):
        """Deletes the node with the given key from the BST.
        Returns True if deletion was successful, False otherwise.
        """
        pass 

    def inorder_traversal(self):
        """Returns a list of keys resulting from an inorder traversal."""
        return self.inorder_recursive([], self.root)
            
    def inorder_recursive(self, res: list, node: TreeNode):
        if node is None:
            return res
        self.inorder_recursive(res, node.left)
        res.append(node.key)
        self.inorder_recursive(res, node.right)
        return res

    def preorder_traversal(self):
        """Returns a list of keys resulting from a preorder traversal."""
        return self.preorder_recursive([], self.root)

    def preorder_recursive(self, res: list, node: TreeNode):
        if node is None:
            return res
        res.append(node.key)
        self.preorder_recursive(res, node.left)
        self.preorder_recursive(res, node.right)
        return res

    def postorder_traversal(self):
        """Returns a list of keys resulting from a postorder traversal."""
        return self.postorder_recursive([], self.root)

    def postorder_recursive(self, res: list, node: TreeNode):
        if node is None:
            return res
        self.postorder_recursive(res, node.left)
        self.postorder_recursive(res, node.right)
        res.append(node.key)
        return res
    #   2
    #  1 3
    # 0   4
    def level_order_traversal(self):
        if self.root is None:
            return []
        res = []
        q = deque()
        q.append(self.root)
        while len(q) > 0:
            curr = q.popleft()
            res.append(curr.key)
            # add children to queue
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        # return res
        return res

    #  0
    # 1 2
    def height(self, node: TreeNode):
        if node is None:
            return 0
        leftHeight = self.height(node.left)
        rightHeight = self.height(node.right)
        return max(leftHeight, rightHeight) + 1

    def size(self, node: TreeNode):
        # count size, return the info to the parent so we can track from above
        if node is None:
            return 0
        leftSize = self.size(node.left)
        rightSize = self.size(node.right)
        return leftSize + rightSize + 1

    def is_balanced(self):
        pass 


import unittest 

class TestBinarySearchTree(unittest.TestCase):
    def test_insert_empty(self):
        bst = BinarySearchTree()
        self.assertIsNone(bst.root)

    def test_insert_single(self):
        bst = BinarySearchTree()
        bst.insert(10)
        self.assertEqual(bst.root.key, 10)
        self.assertIsNone(bst.root.left)
        self.assertIsNone(bst.root.right)

    def test_insert_multiple(self):
        bst = BinarySearchTree()
        bst.insert(20)
        bst.insert(10)
        bst.insert(30)
        self.assertEqual(bst.root.key, 20)
        self.assertEqual(bst.root.left.key, 10)
        self.assertEqual(bst.root.right.key, 30)

    def test_insert_duplicate(self):
        bst = BinarySearchTree()
        bst.insert(20)
        bst.insert(10)
        bst.insert(30)
        bst.insert(20)  # Insert duplicate
        self.assertEqual(bst.inorder_traversal(), [10, 20, 30])  # Should not change

    def test_insert_reverse_order(self):
        bst = BinarySearchTree()
        bst.insert(30)
        bst.insert(20)
        bst.insert(10)
        self.assertEqual(bst.inorder_traversal(), [10, 20, 30])

    def test_insert_large_number(self):
        bst = BinarySearchTree()
        for i in range(1, 101):
            bst.insert(i)
        self.assertEqual(bst.inorder_traversal(), list(range(1, 101)))

    def test_search_empty(self):
        bst = BinarySearchTree()
        self.assertIsNone(bst.search(5))

    def test_search_single(self):
        bst = BinarySearchTree()
        bst.insert(15)
        node = bst.search(15)
        self.assertIsNotNone(node)
        self.assertEqual(node.key, 15)

    def test_search_multiple(self):
        bst = BinarySearchTree()
        bst.insert(25)
        bst.insert(18)
        bst.insert(32)
        bst.insert(12)
        bst.insert(21)
        node = bst.search(18)
        self.assertIsNotNone(node)
        self.assertEqual(node.key, 18)
        node = bst.search(32)
        self.assertIsNotNone(node)
        self.assertEqual(node.key, 32)

    def test_search_not_found(self):
        bst = BinarySearchTree()
        bst.insert(40)
        bst.insert(35)
        bst.insert(45)
        self.assertIsNone(bst.search(50))

    def test_inorder_traversal(self):
        bst = BinarySearchTree()
        bst.insert(20)
        bst.insert(10)
        bst.insert(30)
        bst.insert(5)
        bst.insert(15)
        self.assertEqual(bst.inorder_traversal(), [5, 10, 15, 20, 30])

    def test_preorder_traversal(self):
        bst = BinarySearchTree()
        bst.insert(20)
        bst.insert(10)
        bst.insert(30)
        bst.insert(5)
        bst.insert(15)
        bst.insert(25)
        bst.insert(35)
        self.assertEqual(bst.preorder_traversal(), [20, 10, 5, 15, 30, 25, 35])

    def test_postorder_traversal(self):
        bst = BinarySearchTree()
        bst.insert(20)
        bst.insert(10)
        bst.insert(30)
        bst.insert(5)
        bst.insert(15)
        bst.insert(25)
        bst.insert(35)
        self.assertEqual(bst.postorder_traversal(), [5, 15, 10, 25, 35, 30, 20])

    def test_height_multiple(self):
        # Multi-node tree:
        #      20
        #     /  \
        #    10   30
        #   / \
        #  5  15
        bst = BinarySearchTree()
        bst.insert(20)
        bst.insert(10)
        bst.insert(30)
        bst.insert(5)
        bst.insert(15)
        self.assertEqual(bst.height(bst.root), 3)

    def test_size_empty(self):
        # Empty tree:
        #     (empty)
        bst = BinarySearchTree()
        self.assertEqual(bst.size(bst.root), 0)

    def test_size_single(self):
        # Single node tree:
        #      10
        bst = BinarySearchTree()
        bst.insert(10)
        self.assertEqual(bst.size(bst.root), 1)

    def test_size_multiple(self):
        # Multi-node tree:
        #      20
        #     /  \
        #    10   30
        #   / \
        #  5  15
        bst = BinarySearchTree()
        bst.insert(20)
        bst.insert(10)
        bst.insert(30)
        bst.insert(5)
        bst.insert(15)
        self.assertEqual(bst.size(bst.root), 5)

    def test_level_order(self):
        # Multi-node tree:
        #      20
        #     /  \
        #    10   30
        #   / \
        #  5  15
        bst = BinarySearchTree()
        bst.insert(20)
        bst.insert(10)
        bst.insert(30)
        bst.insert(5)
        bst.insert(15)
        self.assertEqual(bst.level_order_traversal(), [20, 10, 30, 5, 15])

    def test_level_order_empty(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.level_order_traversal(), [])

    def test_level_order_root(self):
        bst = BinarySearchTree()
        bst.insert(1)
        self.assertEqual(bst.level_order_traversal(), [1])

if __name__ == '__main__':
    unittest.main()
