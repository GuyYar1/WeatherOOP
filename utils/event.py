class Event:
    """This file contains the event class to handle events. """
    def __init__(self):
        self.handlers = []
        # breakpoint()

    def __iadd__(self, handler):
        self.handlers.append(handler)
        # breakpoint()
        return self


    def __isub__(self, handler):
        self.handlers.remove(handler)
        return self

    def trigger(self, *args, **kwargs):
        for handler in self.handlers:
            handler(*args, **kwargs)
