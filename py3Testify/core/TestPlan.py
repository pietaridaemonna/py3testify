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
        self.owner = 'owner'
        self.version = '1'
        self.suites = []

    def __repr__(self):
        return "[{\n    \"name\":\"%s\",\n    \"description\":\"%s\",\n    \"suites\":%s\n}]" \
               % (self.name, self.description, self.suites)

    def add_test_suite(self, suite):
        """
        add new TestCase
        """
        self.suites.append(suite)


