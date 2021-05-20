from __future__ import absolute_import, print_function

import unittest, doctest

import pyzmail
from pyzmail.generate import format_addresses


class TestGenerate(unittest.TestCase):
    def test_format_addresses(self):
        """test format_addresse"""
        self.assertEqual(
            'foo@example.com',
            str(
                format_addresses(
                    [
                        'foo@example.com',
                    ]
                )
            ),
        )
        self.assertEqual(
            'Foo <foo@example.com>',
            str(
                format_addresses(
                    [
                        ('Foo', 'foo@example.com'),
                    ]
                )
            ),
        )
        # notice the space around the comma
        self.assertEqual(
            'foo@example.com , bar@example.com',
            str(format_addresses(['foo@example.com', 'bar@example.com'])),
        )
        # notice the space around the comma
        self.assertEqual(
            'Foo <foo@example.com> , Bar <bar@example.com>',
            str(
                format_addresses(
                    [('Foo', 'foo@example.com'), ('Bar', 'bar@example.com')]
                )
            ),
        )


# Add doctest
def load_tests(loader, tests, ignore):
    # this works with python 2.7 and 3.x
    tests.addTests(doctest.DocTestSuite(pyzmail.generate))
    return tests


load_tests.__test__ = False
