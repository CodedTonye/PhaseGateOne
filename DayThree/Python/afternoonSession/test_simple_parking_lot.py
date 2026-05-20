from unittest import TestCase
import simple_parking_lot

class test_simple_parking_lot(TestCase):
    
    def test_that_parking_slot_is_20(self):
        actual = simple_parking_lot.get_parking_slot()
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)
        
    def test_that_9_parking_slot_is_occupied(self):
        actual = simple_parking_lot.get_parking_occupied()
        expected = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)
        
    def test_that_11_parking_slot_is_available(self):
        actual = simple_parking_lot.get_parking_occupied()
        expected = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)
        
    def test_that_more_parking_slot_is_available(self):
        actual = simple_parking_lot.get_parking_available()
        expected = [0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)
        

