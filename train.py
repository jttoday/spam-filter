from features import extract_features

from database import total_hams 
from database import total_spams 
from database import clear_database


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


# add the files in the list 
# to the corpus
def add_files_in_list(listname, corpus):
	with open(listname) as f:
		lines = f.readlines()
		for dirname in lines:
			add_files("corpus/"+dirname.strip(), corpus)

def train_from_corpus(corpus, category):
	for mail in corpus:
		train(read(mail), category)


def auto_train():
	clear_database()
	spams = []
	hams  = []
	add_files_in_list("corpus/spam.list", spams)
	add_files_in_list("corpus/ham.list", hams)
	train_from_corpus(spams, "spam")
	train_from_corpus(hams, "ham")

if __name__=="__main__":
	auto_train()


