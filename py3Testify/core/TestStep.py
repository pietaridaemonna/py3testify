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

    def __repr__(self):
        return "\n                     { \"name\":\"%s\" ,\n                    " \
               "\"command\":%s,\n                    type:%s \n}" % \
               (self.name, self.command, self.type)

