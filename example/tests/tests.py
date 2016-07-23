"""Some simple test cases."""

from unittest import TestCase

from nose.plugins.attrib import attr


def return_true():
    """Returns True."""
    return True


class SimpleTestCase(TestCase):
    """A simple test case to show the different types of tests."""

    def test_unit(self):
        """A simple unit test."""
        self.assertTrue(return_true())

    @attr('wip')
    def test_wip(self):
        """A simple work in progress test."""
        self.assertTrue(not return_true())

    @attr('integration')
    def test_integration(self):
        """A simple integration test."""
        self.assertTrue(return_true())

    @attr('end_to_end')
    def test_end_to_end(self):
        """A simple end to end test."""
        self.assertTrue(return_true())
