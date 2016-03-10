import os
import json
import Image
from nltk.corpus import wordnet as wn

def findSyns(word):
 
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


def findBestMatch(tags):

	pwd = os.getcwd()
	taglist = os.listdir(pwd)
	bestmatch = ''
	bestscore = 0

	for filename in taglist:
		currentscore = 0
		tag = open(filename)
		dic = json.load(tag)
		for word in tags:
			syns = findSyns(word)
			for syn in syns:
				if syn in dic.keys():
					currentscore += float(dic[syn])
		if currentscore>bestscore:
			bestscore = currentscore
			bestmatch = filename
	return bestmatch
chosen = False
while(not chosen):
	bodypart = raw_input("Which body part are you selecting?\n1 for head\n2 for torso\n3 for legs\n")
	if (bodypart=='1'):
		folder = 'heads'
		chosen=True
	elif(bodypart=='2'):
		folder = 'torsos'
		chosen=True
	elif(bodypart=='3'):
		folder = 'legs'
		chosen=True
	else:
		print "Not a valid body part, please input 1 or 2\n"
	
inptlist = raw_input("Enter tags as comma seperated list\n")
inptlist = inptlist.replace(" ", "")
words = inptlist.split(',')

os.chdir('/home/arthur/Documents/Brumhack2015/Untitled-Fighting-Game-With-Clarifai/Tags/' + folder)
name = findBestMatch(words).replace(".py","")

os.chdir('/home/arthur/Documents/Brumhack2015/Untitled-Fighting-Game-With-Clarifai/Images/' + folder)

try:
	img = Image.open(name)
except:
	if(bodypart=='1'):
		img = Image.open('/home/arthur/Documents/Brumhack2015/Untitled-Fighting-Game-With-Clarifai/SPECIAL images/troll.png')
		summons = 'TROLL'
	elif(bodypart=='2'):
		img = Image.open('/home/arthur/Documents/Brumhack2015/Untitled-Fighting-Game-With-Clarifai/SPECIAL images/totem.png')
		summons = 'POLE'
	else:
		img = Image.open('/home/arthur/Documents/Brumhack2015/Untitled-Fighting-Game-With-Clarifai/Images/legs/168.png')
		summons = 'ROBOT TROLL LEGS'

		
	print '/!\\ WARNING! /!\\ NO IMAGE FOUND!'
	print 'SUMMONING THE %s!' % (summons,)
img.show()
del img		
