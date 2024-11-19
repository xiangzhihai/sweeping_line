# Custom Heap Implementation with Deletion: Key Takeaways

## 1. Custom Comparison for Heap Ordering
- Implement `__lt__` method in your object class to define custom ordering
```python
def __lt__(self, other):
    if self.height == other.height:
        return self.start_index < other.start_index
    return self.height > other.height  # For max heap
```
- No need to implement `__eq__` if comparing object identity is sufficient
- For min heap, reverse the comparison
- Handle tie-breaking conditions explicitly

## 2. Lazy Deletion Pattern
```python
class BuildingHeap:
    def __init__(self):
        self.heap = []
        self.removed = set()  # Track removed items
```
Key aspects:
- Keep removed items in a separate set instead of physically removing from heap
- Maintain heap property by only marking items as removed
- Clean up removed items during peek/pop operations
- Memory efficient as heapify not needed for deletion

## 3. Heap Operations with Lazy Deletion
### Push
- Standard heapq push operation
```python
def push(self, item):
    heapq.heappush(self.heap, item)
```

### Peek
```python
def peek(self):
    while self.heap:
        item = self.heap[0]
        if item not in self.removed:
            return item
        heapq.heappop(self.heap)
        self.removed.remove(item)  # Clean up
    return default_value
```

### Pop
```python
def pop(self):
    while self.heap:
        item = heapq.heappop(self.heap)
        if item not in self.removed:
            return item
        self.removed.remove(item)  # Clean up
    return default_value
```

### Remove
```python
def remove(self, item):
    self.removed.add(item)
```

## 4. Benefits and Trade-offs
### Advantages
- O(1) removal operation
- No need to rebuild heap on deletion
- Maintains heap invariant
- Memory efficient for temporary removals

### Disadvantages
- Extra space for removed set
- Delayed cleanup
- Peek/pop operations might need multiple iterations

## 5. Best Practices
1. Clean up removed items during peek/pop operations
2. Use appropriate data structures (set for removed items)
3. Handle empty heap cases
4. Implement clear type hints
5. Write comprehensive unit tests

## 6. Common Use Cases
- Priority queues with dynamic updates
- Event scheduling with cancellation
- Graph algorithms (like Dijkstra's) with updates
- Task scheduling systems

This pattern is particularly useful when:
- Middle deletions are frequent
- Heap rebuild cost is high
- Quick removal is priority
- Memory overhead is acceptable
