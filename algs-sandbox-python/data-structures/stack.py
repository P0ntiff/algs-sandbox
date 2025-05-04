class Stack:
    def __init__(self):
        """Initialise an empty stack"""
        self.stack : list(int) = []

    def push(self, item: int):
        self.stack.append(item)

    def pop(self) -> int: 
        if len(self.stack) == 0:
            raise IndexError
        return self.stack.pop()
    
    def peek(self) -> int:
        if len(self.stack) == 0:
            raise IndexError
        return self.stack[-1]
    
    def isEmpty(self) -> bool:
        return len(self.stack) == 0
    
    def size(self) -> int:
        return len(self.stack)


import unittest

class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push(10)
        self.assertEqual(stack.peek(), 10)
        self.assertEqual(stack.size(), 1)

    def test_pop(self):
        stack = Stack()
        stack.push(20)
        stack.push(30)
        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.peek(), 20)

    def test_pop_empty(self):
        stack = Stack()
        with self.assertRaises(IndexError):  # Assuming you raise IndexError for empty stack
            stack.pop()

    def test_peek(self):
        stack = Stack()
        stack.push(40)
        stack.push(50)
        self.assertEqual(stack.peek(), 50)
        self.assertEqual(stack.size(), 2)  # Peek should not remove elements

    def test_peek_empty(self):
        stack = Stack()
        with self.assertRaises(IndexError):  # Assuming you raise IndexError for empty stack
            stack.peek()

    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.isEmpty())
        stack.push(60)
        self.assertFalse(stack.isEmpty())

    def test_size(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)
        stack.push(70)
        stack.push(80)
        self.assertEqual(stack.size(), 2)

if __name__ == '__main__':
    unittest.main()
