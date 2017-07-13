class TestStep(object):
    """
    high level support for doing this and that.
    """

    def __init__(self, name, _type, command):
        """
        high level support for doing this and that.
        """
        self.name = name
        self.command = command
        self.type = _type
        self.step_number = 0

    def __repr__(self):
        return "\n                             { \n                              " \
               "\"name\":\"%s\" ,\n                              " \
               "\"command\":\"%s\",\n                              " \
               "\"type\":\"%s\",\n                              " \
               "\"step_number\":\"%s\" \n                              }" % \
               (self.name, self.command, self.type, self.step_number)

    def increment_step(self):
        self.step_number += 1
