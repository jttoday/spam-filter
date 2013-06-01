

from data_base import feature_data

class word_feature():
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

def extract_words(text):
	return remove_duplicates(text.lower().split())

def remove_duplicates(t):
	return list(set(t))

def extract_features(text):
	return map(intern_feature, (extract_words(text)))


def intern_feature(word):
	try:
		return feature_data[word]
	except KeyError:
		feature_data[word] = word_feature(word)
		return feature_data[word]


if __name__=="__main__":
	text = raw_input()
	for f in extract_features(text):
		print f
	


