import unittest
import sys

def suite():
    test_suite = unittest.TestSuite()
    all_test_suite = unittest.defaultTestLoader.discover('test', pattern='test_*.py')
    for ts in all_test_suite:
        test_suite.addTest(ts)
    return test_suite

if __name__ == "__main__":
    mySuite = suite()
    isok = unittest.TextTestRunner().run(mySuite).wasSuccessful()
    sys.exit(0 if isok else -1)
