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

    def __repr__(self):
        return "\n         { \"name\":\"%s\" \n        test_cases:%s \n        setup:%s]" % \
               (self.name, self.test_cases, self.setup)

    def add_test_case(self, case):
        """
        add new TestCase
        """
        cas = TestCase(case.name)
        self.test_cases['case'] = cas
