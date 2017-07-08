class TestStep(object):
    """
    high level support for doing this and that.
    """

    def __init__(self, name):
        """
        high level support for doing this and that.
        """
        self.name = name
        self.command = 'n/a'
        self.type = 'shell'

    def set_command(self, comm):
        """
        add new TestCase
        """
        self.command = comm

    def set_type(self, type):
        """
        add new TestCase
        """
        self.type = type
