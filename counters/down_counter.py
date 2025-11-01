from .counter import Counter

class DownCounter(Counter):
    """Counts downwards by step size"""

    def __init__(self, start=0, step=1):
        # call parent constructor
        super().__init__(start, step)

    def count(self):
        """Decrease counter value"""
        self.value -= self.step
        return self.value
