import doctest

import pyzmail


# Add doctest
def load_tests(loader, tests, ignore):
    # this works with python 2.7 and 3.x
    tests.addTests(doctest.DocTestSuite(pyzmail.utils))
    return tests
load_tests.__test__ = False
