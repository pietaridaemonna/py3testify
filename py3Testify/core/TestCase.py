from py3Testify.core.TestStep import TestStep


class TestCase(object):
    """
    high level support for doing this and that.
    """

    def __init__(self, name, descr):
        """
        high level support for doing this and that.
        """
        self.name = name
        self.description = descr
        self.status = 'none'
        self.test_steps = []

    def __repr__(self):
        return "\n                     { \"name\":\"%s\" ,\n                        test_steps:%s \n}" % \
               (self.name, self.test_steps)

    def add_test_step(self, step):
        """
        add new TestCase
        """
        self.test_steps.append(step)



