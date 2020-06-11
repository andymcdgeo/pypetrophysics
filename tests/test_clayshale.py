import unittest
import pypetrophysics.clayshale as cs

#TODO Include tests for all methods

class TestClayShale(unittest.TestCase):
    def test_gr_index(self):
        self.assertAlmostEqual(cs.gr_clay_shale_vol(10, 100, 50), 0.44, delta=0.01)
        self.assertEqual(cs.gr_clay_shale_vol(10, 45, 50, limit_result=True, low_limit=0, high_limit= 1), 1)
        self.assertEqual(cs.gr_clay_shale_vol(55, 100, 50, limit_result=True, low_limit=0, high_limit= 1), 0)

        self.assertAlmostEqual(cs.gr_clay_shale_vol(minvalue=45, maxvalue=135, inputvalue=75, method="larionov-young", limit_result=False, low_limit=0, high_limit= 1), 0.11259, delta=0.01)
        


if __name__ == '__main__':
    unittest.main()