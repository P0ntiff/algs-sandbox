


#     1
#   3   4    --> [0 1 2 3 4 5]
# 9  9 8     --> [1 3 4 9 9 8]
class Heap:
    def __init__(self, higher_priority=lambda x, y: x < y):
        self.heap = []
        # self.higher_priority = higher_priority
    def push(self, item):
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)
    def pop(self):
        # tmp var the root, put the end at the top, then shrink by 1
        if not self.heap:
            return None
        res = self.heap[0]
        if len(self.heap) == 1:
            self.heap = []
            return res
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._bubble_down(0)
        return res
    def top():
        if not self.heap:
            return None 
        return self.heap[0]
    def size():
        return len(self.heap)
    def _bubble_up(self, i):
        # take the last element, just added. 
        # if it's less than its parent, swap and keep going up
        if i == 0:
            return # at the root 
        parent_i = self._parent(i)
        if self.heap[i] < self.heap[parent_i]:
            self.heap[i], self.heap[parent_i] = self.heap[parent_i], self.heap[i]
            return self._bubble_up(parent_i)
    def _bubble_down(self, i):
        # take the top element, if it's smaller than either child, swap and keep going down
        left_i = self._left_child(i)
        right_i = self._right_child(i)
        if not left_i < len(self.heap):
            return
        child_i = left_i
        if right_i < len(self.heap) and self.heap[right_i] < self.heap[left_i]:
            child_i = right_i
        if self.heap[child_i] < self.heap[i]:
            self.heap[i], self.heap[child_i] = self.heap[child_i], self.heap[i]
            self._bubble_down(child_i)
    def heapify(self):
        for i in range(len(self.heap) // 2, -1, -1):
            self._bubble_down(i)
    def _parent(self, i):
        if i > 0:
            return (i - 1) // 2
        return -1
    def _left_child(self, i):
        return 2 * i + 1
    def _right_child(self, i):
        return 2 * i + 2



heap = Heap()
heap.push(4)
heap.push(8)
heap.push(2)
heap.push(6)
heap.push(1)
heap.push(7)
heap.push(3)
heap.push(5)
assert heap.pop() == 1
assert heap.pop() == 2
assert heap.pop() == 3