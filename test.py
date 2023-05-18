import unittest
from asadas import sumar

class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sumar(1, 1), 2)

    def test_2(self):
        self.assertEqual(sumar(1, 3), 4)

    def test_3(self):
        self.assertEqual(sumar(10, 1), 11)

if __name__ == '__main__':
    unittest.main()