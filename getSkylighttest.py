import unittest
from getSkyline_218 import Building, BuildingHeap


class TestBuilding(unittest.TestCase):
    def test_building_creation(self):
        b = Building([1, 5, 10])
        self.assertEqual(b.start_index, 1)
        self.assertEqual(b.end_index, 5)
        self.assertEqual(b.height, 10)

    def test_building_comparison(self):
        b1 = Building([1, 5, 10])
        b2 = Building([2, 6, 8])
        b3 = Building([3, 7, 10])

        # Test height comparison
        self.assertTrue(b1 < b2)  # 10 > 8, so b1 is "less than" b2

        # Test same height, different start
        self.assertTrue(b1 < b3)  # Same height, but b1 starts earlier


class TestBuildingHeap(unittest.TestCase):
    def setUp(self):
        self.heap = BuildingHeap()

    def test_empty_heap(self):
        self.assertEqual(self.heap.peek().height, 0)
        self.assertEqual(self.heap.pop().height, 0)

    def test_push_and_peek(self):
        b1 = Building([1, 5, 10])
        self.heap.push(b1)
        self.assertEqual(self.heap.peek(), b1)

    def test_push_multiple_and_order(self):
        b1 = Building([1, 5, 10])
        b2 = Building([2, 6, 15])
        b3 = Building([3, 7, 12])

        self.heap.push(b1)
        self.heap.push(b2)
        self.heap.push(b3)

        # Should return highest building first
        self.assertEqual(self.heap.peek().height, 15)

        # After removing b2
        self.heap.remove(b2)
        self.assertEqual(self.heap.peek().height, 12)

    def test_remove_and_cleanup(self):
        b1 = Building([1, 5, 10])
        b2 = Building([2, 6, 15])

        self.heap.push(b1)
        self.heap.push(b2)

        # Remove b2
        self.heap.remove(b2)

        # Check if b2 is properly removed
        self.assertEqual(self.heap.peek(), b1)

        # Check if removed set is cleaned up
        self.assertEqual(len(self.heap.removed), 0)

    def test_same_height_ordering(self):
        b1 = Building([2, 5, 10])
        b2 = Building([1, 6, 10])

        self.heap.push(b1)
        self.heap.push(b2)

        # Should return building with earlier start_index first
        self.assertEqual(self.heap.peek(), b2)

    def test_pop_sequence(self):
        buildings = [Building([1, 5, 10]), Building([2, 6, 15]), Building([3, 7, 12])]

        for b in buildings:
            self.heap.push(b)

        # Should pop in order of decreasing height
        self.assertEqual(self.heap.pop().height, 15)
        self.assertEqual(self.heap.pop().height, 12)
        self.assertEqual(self.heap.pop().height, 10)
        self.assertEqual(
            self.heap.pop().height, 0
        )  # Empty heap returns Building([0,0,0])
