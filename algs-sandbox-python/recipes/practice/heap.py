class Heap:
    def __init__(self):
        # min heap solution
        self.heap = [] # length n

    def push(self, item):
        # push onto end of heap, O(logn), bubble up if smaller than its parent
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        # remove top of heap, O(logn)
        # swap top and bottom in O(1), put end of heap on the top, and bubble down till heap restored
        res = self.heap[0]
        popped = self.heap.pop()
        self.heap[0] = popped
        self._bubble_down(0)
        return res

    def _bubble_up(self, i):
        # recursive, swap an element with its parent it < than parent
        if i == 0:
            # at the root, can't bubble up
            return 
        parent_i = self._parent_index(i)
        if self.heap[parent_i] > self.heap[i]:
            self.heap[parent_i], self.heap[i] = self.heap[i], self.heap[parent_i]
            self._bubble_up(parent_i)

    def _bubble_down(self, i):
        # recursively swap an element with its child if > its child
        left_i = self._left_child_index(i)
        right_i = self._right_child_index(i)
        if left_i >= len(self.heap):
            # leaf, no children to swap with
            return
        child_i = left_i 
        # go down the smaller child. TODO Why??
        if right_i < len(self.heap) and self.heap[right_i] < self.heap[left_i]:
            child_i = right_i 
        # swap with child if > than child, else terminate
        if self.heap[i] > self.heap[child_i]:
            self.heap[child_i], self.heap[i] = self.heap[i], self.heap[child_i]
            self._bubble_down(child_i)

    def _parent_index(self, i):
        # get element's parent from the given index 
        if i == 0:
            return None 
        return (i - 1) // 2

    def _left_child_index(self, i):
        return (2 * i) + 1

    def _right_child_index(self, i):
        return (2 * i) + 2




heap = Heap()
heap.push(4)
print(heap.heap)
heap.push(8)
print(heap.heap)
heap.push(2)
print(heap.heap)
heap.push(6)
print(heap.heap)
heap.push(1)
print(heap.heap)
heap.push(7)
print(heap.heap)
heap.push(3)
print(heap.heap)
heap.push(5)
print(heap.heap)
assert heap.pop() == 1
print(heap.heap)
assert heap.pop() == 2
assert heap.pop() == 3