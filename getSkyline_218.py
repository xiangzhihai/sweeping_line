import heapq
from typing import *


class Building:
    def __init__(self, building_input: List[int]) -> None:
        [self.start_index, self.end_index, self.height] = building_input

    def __lt__(self, other):
        # For max heap, we want higher buildings to be "less than" lower buildings
        # If heights are equal, compare by x coordinate
        if self.height == other.height:
            return self.start_index < other.start_index
        return self.height > other.height

    def __repr__(self):
        return f"Building(start={self.start_index}, end={self.end_index}, height={self.height})"


"""
This will be a max heap that saves Building and sorts by 
Building.height. It will also support remove items from middle
of the heap and add item to it. This can be done with a stack 
marking index that can be filled with items. If this stack is 
empty, simply perform normal heap add.

Another way to achieve this is to use a map to mark the 
item as deleted and skip this value if it becomes the top of 
the heap with another heap_pop.
"""
class BuildingHeap:
    def __init__(self):
        self.heap = []
        self.removed: Set[Building] = set()

    def push(self, building: Building):
        heapq.heappush(self.heap, building)

    def pop(self) -> Building:
        while self.heap:
            building: Building = heapq.heappop(self.heap)
            if building not in self.removed:
                return building
            else:
                self.removed.remove(building)
        return Building([0, 0, 0])  # Return when heap is empty

    def remove(self, building: Building):
        self.removed.add(building)

    def peek(self) -> Building:
        while self.heap:
            building: Building = self.heap[0]
            if building not in self.removed:
                return building
            else:
                heapq.heappop(self.heap)
                self.removed.remove(building)
        return Building([0, 0, 0])


class Solution:
    """
    To solve this problem, start by scanning from 0 to right and we need
    to know when we encounter a entry point or exist point, and we need
    to add its height to a data structure that will always tell us the
    heighest point, and when there is an exist point, we need to know
    the next heighest point.

    We need to first sort the entry points and exist points, and generate
    two sorted lists, which only saves the address of the input item,
    here we call it a building. In this way, we can always know which
    point horizontally we will meeting first. For heights, we will build
    a specialized max heap, that saves buildings and is ordered by the
    height. It will also support the removing a building in middle of
    the heap, and add items to a heap with empty leaves. This will ensure
    us that we can always get the heighest height.

    To generate the result, we just need to take a note of the heap's root
    value changes. The heap will start with a 0 value to mark the land.

    Time complexity: O(N * log(N)) ---- Sorting takes O(N log(N)) and sweeping
        horizontally takes O(N) * and vertically takes O(log(n)) and these
        together are still O(N * log(N)).
    Space Complexity: O(N) ---- Size of two sorted list and heap.
    """

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        building_obj_list = [
            Building(building_list_item) for building_list_item in buildings
        ]
        sorted_start_list = sorted(
            building_obj_list, key=lambda building: building.start_index
        )
        sorted_end_list = sorted(
            building_obj_list, key=lambda building: building.end_index
        )
