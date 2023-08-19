class NegativeNumberException(Exception):
    def __init__(self, value):
        if value < 0:
            self.value = value
            super().__init__("Negative value cannot be input")