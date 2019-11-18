class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        if (self.capacity - v) >= 0:
            return True
        else:
            return False

    def add(self, v):
        if  self.can_add(v):
            self.capacity -= v
