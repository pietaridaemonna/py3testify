
class TestData(object):
    """
    high level support for doing this and that.
    """

    def __init__(self, name, descr):
        """
        high level support for doing this and that.
        """
        self.name = name
        self.description = descr
        self.data = []

    def __repr__(self):
        return "\n                     { \n                     " \
               "\"name\":\"%s\" ,\n                     " \
               "\"description\":\"%s\" ,\n                     " \
               "\"data\":%s \n                      }" % \
               (self.name, self.description, self.data)

    def add_test_step(self, step):
        """
        add new TestCase
        """
        self.test_steps.append(step)