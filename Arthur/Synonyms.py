from nltk.corpus import wordnet as wn

def getSyns(word):
	try:
		read = wn.synsets(word)[0].name()
	except:
		return [word]
	

	syn = wn.synset(read)

	synsets = syn.lemma_names()
	hypernyms = syn.hypernyms()

	synsets = [x.replace('_',' ') for x in synsets]
	hypernyms = [x.name().split('.')[0].replace('_',' ') for x in hypernyms]

	return synsets + hypernyms

word = raw_input()

for i in getSyns(word):
	print i
