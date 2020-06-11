import unittest
import pypetrophysics.miscfuncs as mf

class TestMiscFuncs(unittest.TestCase):
    def test_limit_vals(self):
        self.assertEqual(mf.limit_vals(0.56, 0, 0.5), 0.5)
        self.assertEqual(mf.limit_vals(0.56, 0.6, 1), 0.6)
        self.assertEqual(mf.limit_vals(0.56, 0, 0.56), 0.56)
        
    def test_dec_perc_convert(self):
        self.assertEqual(mf.dec_perc_convert(50, "percent"), 0.5)
        self.assertEqual(mf.dec_perc_convert(0.23, "decimal"), 23)