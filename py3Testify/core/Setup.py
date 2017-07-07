class Setup(object):
    """
    Method called to prepare the test fixture. This is called immediately before calling the test method; 
    other than AssertionError or SkipTest, any exception raised by this method will be considered an error rather than a test failure. 
    A test fixture represents the preparation needed to perform one or more tests, and any associate cleanup actions.
    This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.
    """

    def __init__(self, name):
        """
        high level support for doing this and that.
        """
        self.name = name

    def add_test_suite(self):
        """
        add new TestCase
        """
        print('destroying  ' + self.name)

    def add_test_case(self):
            """
        add new TestCase
        """
        print('destroying  ' + self.name)