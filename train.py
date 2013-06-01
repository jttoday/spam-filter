from features import extract_features

from data_base import total_hams 
from data_base import total_spams 


def train(text, category):
	for f in extract_features(text):
		increase_count(f, category)
		increase_total_count(category)

def increase_count(feature, category):
	if category == "ham":
		feature.increase_ham()
	elif category == "spam":
		feature.increase_spam()

def increase_total_count(category):
	if category == "ham":
		total_hams.increase()
	elif category == "spam":
		total_spams.increase()


