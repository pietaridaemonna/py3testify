from py3Testify.core.TestStep import TestStep


class TestCase(object):
    """
    high level support for doing this and that.
    """

    def __init__(self, name):
        """
        high level support for doing this and that.
        """
        self.name = name
        self.status = 'none'
        self.test_steps = {}

    def __repr__(self):
        return "<Test a:%s b:%s c:%s>" % (self.name, self.status, self.test_steps)

    def add_test_step(self, name, type, command):
        """
        add new TestCase
        """
        step = TestStep(name)
        step.set_command(command)
        step.set_type(type)

        self.test_steps['step'] = step


