import unittest
from my_package.module import hello_world

class TestModule(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), 'Hello, world!')

if __name__ == '__main__':
    unittest.main()
