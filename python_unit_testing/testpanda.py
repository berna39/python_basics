import unittest
from panda import Panda

class TestPanda(unittest.TestCase):
    def setUp(self):
        self.po = Panda('Poo', 12)

    def tearDown(self):
        pass

    def test_panda_is_instance_of_panda(self):
        self.assertIsInstance(self.po, Panda)

    def test_panda_age_is_positive(self):
        print(self.po)
        self.assertGreater(self.po.age, 0)

if __name__ == '__main__':
    unittest.main()
