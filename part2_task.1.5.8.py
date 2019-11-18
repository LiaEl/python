class MoneyBox:
    def __init__(self, capacity):
    	self.capacity = capacity
    	self.coins = 0

    def can_add(self, v):
    	self.add_coins = v
    	if self.coins + self.add_coins <= self.capacity:
    		return True
    	else:
        	return False

    def add(self, v):
    	self.coins += v