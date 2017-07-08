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
        self.suites = []
        print('|' + self.name)

    def add_test_suite(self, suite):
        """
        add new TestCase
        """
        sut = TestSuite(suite.name)
        self.suites.append(sut)

        #print(self.name + ' adding test_suite  ' + suite.name)

