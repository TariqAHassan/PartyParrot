"""

    Conversion Tests
    ~~~~~~~~~~~~~~~~

"""
import os
import sys
import unittest

# Allow access to modules
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("../"))

from party_parrot import to_parrot, from_parrot

test_string = "hello world!!!:3u383::484:::!:!"

class ConversionTests(unittest.TestCase):

    def test_conversion(self, key=1):
        conversion = from_parrot(to_parrot(test_string, key=key), key=key)
        self.assertEqual(conversion, test_string)

    def test_key(self):
        for k in (1, 35, 99, 180):
            _ = self.test_conversion(key=k)


unittest.main()
