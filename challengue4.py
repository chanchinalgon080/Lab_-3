class MinHeap:
    def __init__(self):
        self.heap = []  # Initializes the heap as an empty list

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent] > self.heap[index]:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                index = parent
            else:
                break

    def delete_min(self):
        if not self.heap:
            return None  # Return None if the heap is empty

        # Swap the root with the last element and remove the last element
        min_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        # Restore the heap property starting from the root
        self._heapify_down(0)

        return min_value

    def _heapify_down(self, index):
        n = len(self.heap)
        while index < n:
            smallest = index
            left = 2 * index + 1  # Left child index
            right = 2 * index + 2  # Right child index

            # Check if the left child is smaller than the current node
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            # Check if the right child is smaller than the current node
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            # If the node is already the smallest, break out of the loop
            if smallest == index:
                break

            # Swap the node with the smallest child
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            # Update the index and continue the heapify process
            index = smallest

# 🧪 Test cases


def test_min_heap_delete_min():
    h = MinHeap()
    # Test when the heap is empty, should return None
    print("🧹 Test 1:", h.delete_min() is None)
    h.heap = [1]
    # Test single element heap
    print("🧹 Test 2:", h.delete_min() == 1 and h.heap == [])
    h.heap = [1, 3, 2]
    print("🧹 Test 3:", h.delete_min() == 1 and h.heap ==
          [2, 3])  # Test with 3 elements
    h.heap = [1, 3, 4, 5]
    print("🧹 Test 4:", h.delete_min() == 1 and h.heap ==
          [3, 5, 4])  # Test with 4 elements
    h.heap = [1, 2, 3, 4, 5]
    min_val = min(h.heap)
    # Test with multiple elements
    print("🧹 Test 5:", h.delete_min() == min_val)


test_min_heap_delete_min()
