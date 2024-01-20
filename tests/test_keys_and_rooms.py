import unittest
from src.keys_and_rooms import canVisitAllRooms


class TestKeysAndRooms(unittest.TestCase):
    def test_all_rooms_accessible(self):
        """
        Test if all rooms are accessible when they should be.
        """
        self.assertTrue(canVisitAllRooms([[1], [2], [3], []]))

    def test_some_rooms_inaccessible(self):
        """
        Test if the function correctly identifies when not all rooms are accessible.
        """
        self.assertFalse(canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))

    # Additional test methods can be added here


if __name__ == "__main__":
    unittest.main()
