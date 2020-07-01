#https://stackoverflow.com/questions/1732438/how-do-i-run-all-python-unit-tests-in-a-directory
import unittest

loader = unittest.TestLoader()

start_dir = 'tests/'

suite = loader.discover(start_dir)

result = unittest.TextTestRunner().run(suite)

if result.wasSuccessful():
    exit(0)
else:
    exit(1)