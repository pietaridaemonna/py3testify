class Teardown(object):
    """
    Method called immediately after the test method has been called and the result recorded.
    This is called even if the test method raised an exception, so the implementation in subclasses 
    may need to be particularly careful about checking internal state.
    """

    def __init__(self, name, values):
        """
        high level support for doing this and that.
        """
        self.name = name
        self.values = values

