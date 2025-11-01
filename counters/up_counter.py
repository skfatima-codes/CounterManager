from .counter import Counter

class UpCounter(Counter):
    """Counts upwards by step size"""

    def __init__(self, start=0, step=1):
        # call parent constructor
        super().__init__(start, step)

    def count(self):
        """Increase counter value"""
        self.value += self.step
        return self.value
