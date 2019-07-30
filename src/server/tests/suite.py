import unittest
from config_test import TestConfigParser
from factory_test import TestFactory
from dao_test import TestDao

def suite():
    """
    Suite of unit and integration tests for the Journal api
    :return:
    """
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    test_suite.addTests(TestConfigParser)
    test_suite.addTests(TestFactory)
    test_suite.addTests(TestDao)

    # initialize a runner, pass it your suite and run it
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(test_suite)

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
