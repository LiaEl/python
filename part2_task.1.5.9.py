class Buffer:
    def __init__(self):
    	self.list = []

    def add(self, *a):
    	self.list += a
    	while len(self.list) >= 5:
    		print(sum(self.list[:5]))
    		self.list = self.list[5:]

    def get_current_part(self):
    	return self.list