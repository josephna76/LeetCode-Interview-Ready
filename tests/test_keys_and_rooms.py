import unittest
from src.keys_and_rooms import canVisitAllRooms
from utils.utils import print_colored


class TestKeysAndRooms(unittest.TestCase):
    def test_all_rooms_accessible(self):
        result = canVisitAllRooms([[1], [2], [3], []])
        message = "Test All Rooms Accessible: Expected True, got {}".format(result)
        print_colored(message, "pass" if result else "fail")
        self.assertTrue(result)

    def test_some_rooms_inaccessible(self):
        result = canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]])
        message = "Test Some Rooms Inaccessible: Expected False, got {}".format(result)
        print_colored(message, "pass" if not result else "fail")
        self.assertFalse(result)

    # ... (other tests follow the same pattern)


if __name__ == "__main__":
    unittest.main()
