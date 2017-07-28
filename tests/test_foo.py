from unittest import TestCase

from qgeneration import functions


class TestFoo(TestCase):
    def test_foo(self):
        s = functions.foo()
        self.assertEqual(s, "bar")
