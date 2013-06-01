

from data_base import feature_data

def extract_words(text):
	return remove_duplicates(text.lower().split())

def remove_duplicates(t):
	return list(set(t))

def extract_features(text):
	return map(to_feature, (extract_words(text)))


def to_feature(word):
	return feature_data.get(word)


if __name__=="__main__":
	text = raw_input()
	for f in extract_features(text):
		print f
	


