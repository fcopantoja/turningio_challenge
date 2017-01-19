import unittest
from palindrome import base10_to_n, is_palindrome, lowest_base_palindrome


class PalindromeTestCase(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('1331'))
        self.assertTrue(is_palindrome('33133'))
        self.assertTrue(is_palindrome('aibohphobia'))
        self.assertTrue(is_palindrome('detartrated'))

        self.assertFalse(is_palindrome('Lorem'))
        self.assertFalse(is_palindrome('Ipsum'))
        self.assertFalse(is_palindrome('dolor'))
        self.assertFalse(is_palindrome('consectetur'))
        self.assertFalse(is_palindrome('amet'))

    def test_base10_to_n(self):
        n = 20
        hexadecimal = '{0:x}'.format(n)
        octal = '{0:o}'.format(n)
        binary = '{0:b}'.format(n)
        self.assertEquals(base10_to_n(n, 16), hexadecimal)
        self.assertEquals(base10_to_n(n, 8), octal)
        self.assertEquals(base10_to_n(n, 2), binary)
        self.assertEquals(base10_to_n(n, 10), str(n))

        n = 6932
        hexadecimal = '{0:x}'.format(n)
        octal = '{0:o}'.format(n)
        binary = '{0:b}'.format(n)
        self.assertEquals(base10_to_n(n, 16), hexadecimal)
        self.assertEquals(base10_to_n(n, 8), octal)
        self.assertEquals(base10_to_n(n, 2), binary)
        self.assertEquals(base10_to_n(n, 10), str(n))

    def test_lowest_base_palindrome(self):
        palindrome, base = lowest_base_palindrome(28)
        self.assertEquals(palindrome, '1001')
        self.assertEquals(base, 3)

        palindrome, base = lowest_base_palindrome(93)
        self.assertEquals(palindrome, '1011101')
        self.assertEquals(base, 2)


def main():
    unittest.main()
