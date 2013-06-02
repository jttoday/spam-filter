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

# need some clean up
# train from corpus
from os import listdir
from os.path import join

# add all files to the corpus database
def add_files(dirname, corpus):
	files = map(lambda(x):join(dirname, x), listdir(dirname))
	corpus.extend(files)


def read(filename):
	infile = open(filename, 'r')
	return infile.read()

def train_from_corpus(corpus, category):
	for mail in corpus:
		train(read(mail), category)


