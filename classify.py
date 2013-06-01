from math import log
from math import exp

from features import word_feature
from features import extract_features
from data_base import total_spams
from data_base import total_hams

MIN_SPAM_SCORE = 0.6
MAX_HAM_SCORE = 0.4


def classify(text):
	s = score(extract_features(text))
	print s
	if s <= MAX_HAM_SCORE:
		return "ham"
	elif s>= MIN_SPAM_SCORE:
		return "spam"
	else:
		return "unsure"

# Reference Gray Robinson's "A statistical Approach to the Spam Problem"
# for the functions to calculate the probablity of spam


#This is a naive implement of calculating spam probability
def spam_probability(feature):
	spam = feature.spam_count
	ham  = feature.ham_count
	spam_frequency = 1.0* spam / max(1, total_spams.num())
	ham_frequency  = 1.0* ham  / max(1, total_hams.num())
	return spam_frequency / (ham_frequency + spam_frequency)

#This uses Robinson's paper to calculate spam probability of certain word
def bayesian_spam_probability(feature, assumed_probability = 0.5, weight = 1):
	basic_probability = spam_probability(feature)
	data_points = feature.spam_count + feature.ham_count
	# Robinson's function
	return 1.0* (assumed_probability * weight + data_points * basic_probability) / ( weight + data_points)

#Use R.A.Fisher method to score a feature
#In fact, I am not very clear about the reason why it works well.
#I just copy it and translate into python
def score(features):
	spam_probs = [] #prob == probability
	ham_probs  = []
	number_probs = 0
	for feature in features:
		if not feature.trained():
			spam_prob = bayesian_spam_probability(feature)
			spam_probs.append(spam_prob)
			ham_probs.append(1.0 - spam_prob)
			number_probs += 1
	h = 1 - fisher(spam_probs, number_probs)
	s = 1 - fisher(ham_probs,  number_probs)
	return (1-h+s)/2.0


#Still Fisher's method
#Not understood neither
def fisher(probs, number_probs):
	v = reduce(lambda x,y:x+y,  map(log,probs), 0)
	return inverse_chi_square(-2 * v , 2 * number_probs)


# Copy this function from following website
# http://www.linuxjournal.com/files/linuxjournal.com/linuxjournal/articles/064/6467/6467s2.html
# The algorithms is beyond my reach 
def inverse_chi_square(value, freedom):
	m = value / 2.0
	sum = term = exp(-m)
	for i in range(1, freedom/2):
		term *= m / i
		sum += term
    # With small chi and large df, accumulated
    # roundoff error, plus error in
    # the platform exp(), can cause this to spill
    # a few ULP above 1.0. For
    # example, chi2P(100, 300) on my box
    # has sum == 1.0 + 2.0**-52 at this
    # point.  Returning a value even a teensy
    # bit over 1.0 is no good.
	return min(sum, 1.0)


if __name__=="__main__":
	from train import train
	train("Make money fast", "spam")
	train("Do you have money for the movies?", "ham")
	print classify("Make money fast")
	print classify("Want to go to the movies?")



