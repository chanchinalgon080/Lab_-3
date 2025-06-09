class MinHeap:
    def __init__(self):
        self.heap = []  # Initializes the heap as an empty list

    def build_heap(self, array):
        self.heap = array[:]  # Makes a shallow copy of the given array
        # Calculate the index of the last non-leaf node
        start_idx = (len(self.heap) // 2) - 1
        # Apply _heapify_down from the last non-leaf node up to the root
        for i in range(start_idx, -1, -1):
            self._heapify_down(i)

    def _heapify_down(self, index):
        heap = self.heap
        n = len(heap)
        # Loop to ensure the node at 'index' satisfies the min-heap property
        while index < n:
            smallest = index
            left = 2 * index + 1  # Left child index
            right = 2 * index + 2  # Right child index

            # Check if the left child is smaller than the current node
            if left < n and heap[left] < heap[smallest]:
                smallest = left
            # Check if the right child is smaller than the current node
            if right < n and heap[right] < heap[smallest]:
                smallest = right

            # If the node is already the smallest, break out of the loop
            if smallest == index:
                break

            # Swap the node with the smallest child
            heap[index], heap[smallest] = heap[smallest], heap[index]
            # Update the index and repeat the process with the smallest child
            index = smallest

# 🧪 Test cases


def test_build_heap():
    h = MinHeap()
    h.build_heap([5, 3, 8, 1, 2])
    # Expecting the min-heap to have the minimum value at the root
    print("🔨 Test 1:", h.heap[0] == min([5, 3, 8, 1, 2]))
    h.build_heap([7, 6, 5, 4, 3, 2, 1])
    # The minimum value in this array should be 1
    print("🔨 Test 2:", h.heap[0] == 1)
    h.build_heap([2, 1])
    print("🔨 Test 3:", h.heap == [1, 2])  # Expecting the heap to be [1, 2]
    h.build_heap([10])
    # The heap should be [10] when there is only one element
    print("🔨 Test 4:", h.heap == [10])
    h.build_heap([])
    # An empty array should result in an empty heap
    print("🔨 Test 5:", h.heap == [])


test_build_heap()
