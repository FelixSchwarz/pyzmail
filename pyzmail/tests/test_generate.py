# -*- coding: UTF-8 -*-

from __future__ import absolute_import, print_function

import unittest, doctest

import pyzmail
from pyzmail.generate import build_mail, complete_mail, format_addresses, Attachment


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

    def test_build_mail_with_attachment(self):
        attachment = Attachment(
            data=b'pdf-content',
            maintype='application',
            subtype='pdf',
            filename=u'äöü.pdf',
        )
        msg_body = build_mail(
            ('plain text', 'utf8'), attachments=[attachment], use_quoted_printable=True
        )
        msg_meta = complete_mail(
            msg_body,
            'sender@site.example',
            ('recipient@site.example',),
            subject=u'subject',
            default_charset='utf8',
        )
        msg_str = msg_meta[0]

        msg = pyzmail.message_from_string(msg_str)
        self.assertEqual(2, len(msg.mailparts))
        text_part, attachment_part = msg.mailparts
        self.assertEqual(u'äöü.pdf', attachment_part.filename)


# Add doctest
def load_tests(loader, tests, ignore):
    # this works with python 2.7 and 3.x
    tests.addTests(doctest.DocTestSuite(pyzmail.generate))
    return tests


load_tests.__test__ = False
