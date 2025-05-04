
class LLNode:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def enqueue(self, item):
        new_head = LLNode(item)
        if self.head is not None:
            new_head.next = self.head 
        self.head = new_head
        if self.tail is None:
            self.tail = self.head
        self.length += 1

    def dequeue(self):
        res = self.tail
        if res is None:
            raise IndexError
        # set new tail
        next_pointer = new_tail = self.head
        if next_pointer is not None:
            while next_pointer.next:
                new_tail = next_pointer
                next_pointer = next_pointer.next 
        self.tail = new_tail
        self.length -= 1
        return res.val

    def peek(self):
        if self.tail:
            return self.tail.val
        raise IndexError 

    def size(self) -> int:
        return self.length

    def is_empty(self) -> bool:
        if self.head is None:
            return True
        return False

import unittest

class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(10)
        self.assertEqual(queue.peek(), 10)
        self.assertEqual(queue.size(), 1)

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(20)
        queue.enqueue(30)
        self.assertEqual(queue.dequeue(), 20)
        self.assertEqual(queue.size(), 1)
        self.assertEqual(queue.peek(), 30)

    def test_dequeue_empty(self):
        queue = Queue()
        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_peek(self):
        queue = Queue()
        queue.enqueue(40)
        queue.enqueue(50)
        self.assertEqual(queue.peek(), 40)
        self.assertEqual(queue.size(), 2)

    def test_peek_empty(self):
        queue = Queue()
        with self.assertRaises(IndexError):
            queue.peek()

    def test_is_empty(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())
        queue.enqueue(60)
        self.assertFalse(queue.is_empty())

    def test_size(self):
        queue = Queue()
        self.assertEqual(queue.size(), 0)
        queue.enqueue(70)
        queue.enqueue(80)
        self.assertEqual(queue.size(), 2)

if __name__ == '__main__':
    unittest.main()