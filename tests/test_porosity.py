import unittest
# from pypetrophysics.porosity import Porosity
from pypetrophysics.porosity import Porosity


class TestPorosity(unittest.TestCase):
    poro = Porosity()

    def test_porosity_density(self):
        self.assertAlmostEqual(self.poro.porosity_density(2.65, 1, 2.45), 0.1379, delta=0.01)
        self.assertAlmostEqual(self.poro.porosity_density(2.71, 1, 2.45), 0.1793, delta=0.01)
        
        self.assertEqual(self.poro.porosity_density(2.65, 1, 2.64, limit_result=True, low_limit=0.1, high_limit=1), 0.1)
        self.assertEqual(self.poro.porosity_density(2.65, 1, 2.24, limit_result=True, low_limit=0, high_limit=0.12), 0.12)

    def test_porosity_sonic(self):
        self.assertAlmostEqual(self.poro.porosity_sonic(55, 189, 75),0.1481, delta=0.01)

    def test_random(self):
        self.assertTrue(True)
    
if __name__ == '__main__':
    unittest.main()