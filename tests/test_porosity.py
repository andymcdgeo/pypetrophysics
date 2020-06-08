import unittest
from pypetrophysics import porosity

class TestPorosity(unittest.TestCase):
    poro = porosity.Porosity()

    def test_porosity_density(self):
        self.assertAlmostEqual(self.poro.porosity_density(2.65, 1, 2.45), 0.1379, delta=0.01)
        self.assertAlmostEqual(self.poro.porosity_density(2.71, 1, 2.45), 0.1793, delta=0.01)
        
        self.assertEqual(self.poro.porosity_density(2.65, 1, 2.64, limit_result=True, low_limit=0.1, high_limit=1), 0.1)
        self.assertEqual(self.poro.porosity_density(2.65, 1, 2.24, limit_result=True, low_limit=0, high_limit=0.12), 0.12)
    
if __name__ == '__main__':
    unittest.main()