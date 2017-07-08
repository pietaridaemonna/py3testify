from py3Testify.core.TestCase import TestCase


class TestSuite(object):
    """
    high level support for doing this and that.
    """

    def __init__(self, name):
        """
        high level support for doing this and that.
        """
        self.name = name
        self.test_cases = {}
        self.setup = {}
        self.teardown = {}

    def add_test_case(self, case):
        """
        add new TestCase
        """
        cas = TestCase(case.name)
        self.test_cases['case'] = cas
