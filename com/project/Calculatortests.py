import unittest
import sys
from com.project import Calculator


class TestCalculatorMethods(unittest.TestCase):
    def testCalculator(self):
        print sys.modules[__name__]
        self.assertEqual(Calculator.square(2), 4)
        pass


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    # unittest.main()

    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculatorMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)

