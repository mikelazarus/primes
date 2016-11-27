from unittest import TestCase


class TestIs_prime(TestCase):
    def test_is_prime(self):
        from check_prime import is_prime
        self.assertTrue(is_prime(5))


    def test_is_not_prime(self):
        from check_prime import is_prime
        self.assertFalse(is_prime(6))
