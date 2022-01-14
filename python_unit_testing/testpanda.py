import unittest
from panda import Panda

class TestPanda(unittest.TestCase):
    def test_panda_is_instance_of_panda(self):
        po = Panda('Poo', 12)
        self.assertIsInstance(po, Panda)

    def test_panda_age_is_positive(self):
        po = Panda('Poo', 12)
        self.assertGreater(po.age, 0)

if __name__ == '__main__':
    unittest.main()
