from abc import ABC, abstractmethod

class Counter(ABC):
    """Abstract Base Counter class for Up and Down counters"""

    def __init__(self, start=0, step=1):
        self.start = start      # initial starting value
        self.value = start      # current value
        self.step = step        # step increment/decrement

    @abstractmethod
    def count(self):
        """Abstract method to be implemented by subclasses"""
        pass

    def reset(self):
        """Reset counter to start value"""
        self.value = self.start

    def get_value(self):
        """Return current counter value"""
        return self.value

    def __str__(self):
        return f"Current Value → {self.value}"
