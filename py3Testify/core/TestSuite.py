from py3Testify.core.TestCase import TestCase


class TestSuite(object):
    """
    high level support for doing this and that.
    """

    def __init__(self, name, descr):
        """
        high level support for doing this and that.
        """
        self.name = name
        self.description = descr
        self.test_cases = []
        self.setup = {}
        self.teardown = {}

    def __repr__(self):
        return "\n              {\n               \"name\":\"%s\"," \
               "\n               \"description\":\"%s\",\n               \"test" \
               "_cases\":%s,\n               \"setup\":%s,\n               \"teardown\":%s\n              }" % \
               (self.name, self.description, self.test_cases, self.setup, self.teardown)

    def add_test_case(self, case):
        """
        add new TestCase
        """
        self.test_cases.append(case)

