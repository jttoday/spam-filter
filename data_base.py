
class Feature():
	def __init__(self, word):
		self.word = word
		self.spam_count = 0
		self.ham_count  = 0

	def __str__(self):
		return "{0} hams: {1} spams: {2}".format(self.word, self.ham_count, self.spam_count)

	def increase_ham(self):
		self.ham_count  += 1
	
	def increase_spam(self):
		self.spam_count += 1

	# Used in classify.score()
	# May be not suitable to be a member function
	def trained(self):
		return self.spam_count+self.ham_count == 0



class Counter():
	def __init__(self,n = 0):
		self.n = n

	def increase(self):
		self.n += 1

	def num(self):
		return self.n

	def clear(self):
		self.n = 0

class Feature_data():
	def __init__(self):
		self.data = {}

	def get(self, word):
		try:
			return self.data[word]
		except KeyError:
			self.data[word] = Feature(word)
			return self.data[word]

	def clear(self):
		self.data = {}


feature_data = Feature_data()	#storing word feature class
total_hams  = Counter() 
total_spams = Counter()

def clear_database():
	feature_data.clear()
	total_hams.clear()
	total_spams.clear()


