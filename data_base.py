


class Counter():
	def __init__(self,n = 0):
		self.n = n

	def increase(self):
		self.n += 1

	def num(self):
		return self.n

feature_data = {}	#storing word feature class
total_hams  = Counter() 
total_spams = Counter()

def clear_database():
	feature_data = {}
	total_hams  = Counter(0)
	total_spams = Counter(0)


