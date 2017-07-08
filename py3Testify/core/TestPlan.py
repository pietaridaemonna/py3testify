from py3Testify.core.TestSuite import TestSuite


class TestPlan(object):
    """
    high level support for doing this and that.
    """

    def __init__(self, name, description):
        """
        high level support for doing this and that.
        """
        self.name = name
        self.description = description
        self.suites = {}

    def __repr__(self):
        return "<Plan name:%s \ndescription:%s \nsuites:%s>" % (self.name, self.description, self.suites)

    def add_test_suite(self, suite):
        """
        add new TestCase
        """
        sut = TestSuite(suite.name)
        self.suites['suite'] = sut


