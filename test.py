import unittest
from board import Board
import numpy as np

class TestBoard(unittest.TestCase):

    def test_create(self):
        b = Board()
        
        equal_elements = np.sum(b.data == np.ones((3,3))*-1)
        self.assertEqual(equal_elements,9)

    def test_set_piece(self):
        b = Board()
        b.set_piece(1,0,0)
        
        result = np.array([[1,-1,-1],[-1,-1,-1],[-1,-1,-1]])
        print(b.data)
        equal_elements = np.sum(b.data == result)
        self.assertEqual(equal_elements,9)

    def test_has_won(self):
        b = Board()
        b.set_piece(1,0,0)
        b.set_piece(1,1,1)
        b.set_piece(1,2,2)
        
        self.assertEqual(b.has_won(1),True)

if __name__ == '__main__':
    unittest.main()