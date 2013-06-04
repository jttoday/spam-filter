import shelve		# using shelve as persistence manager
import os			# to delete existing files for clear()

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

db_name = "spam_filter.db"
myShelve = shelve.open(db_name, writeback = True)


class Counter():
	def __init__(self, name):
		self.n = 0

	def increase(self):
		self.n += 1

	def num(self):
		return self.n

	def clear(self):
		self.n = 0

	
class Counter_data():
	def get(self, name):
		try:
			return myShelve[name]
		except KeyError:
			myShelve[name] = Counter(name)
			return myShelve[name]

class Feature_data():
	def get(self, word):
		try:
			return myShelve[word]
		except KeyError:
			myShelve[word] = Feature(word)
			return myShelve[word]


feature_data = Feature_data()	#storing word feature class
counter_data = Counter_data()
total_hams  = counter_data.get("hams_total_amount") 
total_spams = counter_data.get("spams_total_amount")

def clear_database():
#	os.remove(db_name)
#	myShelve = shelve.open(db_name, writeback = True)
	return 0



if __name__=="__main__":
	feature_data.get("word").increase_ham()
	feature_data.get("word").increase_spam()
	total_hams.increase() 
	print feature_data.get("word")
	print total_hams.n
	myShelve.close()

