from py3Testify.core import TestSuite

class TestPlan(object):
    """
    high level support for doing this and that.
    """

    def __init__(self, name):
        """
        high level support for doing this and that.
        """
        self.name = name
        self.suites = []

    def add_test_suite(self, suite):
        """
        add new TestCase
        """
        print('destroying  ' + self.name)

    def add_setup(self):
        """
        add new TestCase
        """
        print('destroying  ' + self.name)

    def add_teardown(self):
        """
        add new TestCase
        """
        print('destroying  ' + self.name)
