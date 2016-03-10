import os
import json
import Image
from nltk.corpus import wordnet as wn
import random
import shutil

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

#replace or create file destination folder so that it is empty
dest = '/home/arthur/Documents/Brumhack2015/Untitled-Fighting-Game-With-Clarifai/Sprites/'
try:
	shutil.rmtree(dest)
except:
	pass
os.mkdir(dest)

#iterate through parts, getting most relevant pic and setting troll if none found
parts = ['heads','torsos','legs']
backgroundtags = []
trollparts = 0
for part in parts:
	inptlist = raw_input("Enter single-word tags for the " + part + " as comma seperated list\n")
	inptlist = inptlist.replace(" ", "")
	words = inptlist.split(',')
	backgroundtags += words		#input is now in array of words

	os.chdir('/home/arthur/Documents/Brumhack2015/Untitled-Fighting-Game-With-Clarifai/Tags/' + part)
	name = findBestMatch(words).replace(".py","")
	os.chdir('/home/arthur/Documents/Brumhack2015/Untitled-Fighting-Game-With-Clarifai/Images/' + part)
	outputimg = os.getcwd() +'/' + name	#this now contains the location of the file to copy
	try:
		shutil.copy(outputimg, dest + '/' + part)	#copy to the destination folder, with name of the current part
	except:
		if(part=='heads'):
			shutil.copy('/home/arthur/Documents/Brumhack2015/Untitled-Fighting-Game-With-Clarifai/SPECIAL images/troll.png', dest + '/' + part)
			summons = 'TROLL'
		elif(part=='torsos'):
			shutil.copy('/home/arthur/Documents/Brumhack2015/Untitled-Fighting-Game-With-Clarifai/SPECIAL images/totem.png', dest + '/' + part)
			summons = 'POLE'
		else:
			shutil.copy('/home/arthur/Documents/Brumhack2015/Untitled-Fighting-Game-With-Clarifai/SPECIAL images/hole.png', dest + '/' + part)
			summons = 'HOLE'

		trollparts+=1		
		print '/!\\ WARNING! /!\\ NO IMAGE FOUND!\nSUMMONING THE %s!' % (summons,)

if trollparts==3:
	os.chdir('/home/arthur/Documents/Brumhack2015/Untitled-Fighting-Game-With-Clarifai/SPECIAL images/')
	name = 'totempole.png'
	shutil.copy(os.getcwd() +'/'+ name, dest + '/backgrounds')
	print '/!\\ WARNING! /!\\ THE TOTEM HAS BEEN SUMMONED!'
else:

	os.chdir('/home/arthur/Documents/Brumhack2015/Untitled-Fighting-Game-With-Clarifai/Tags/backgrounds')
	name = findBestMatch(backgroundtags).replace(".py", "")
	os.chdir('/home/arthur/Documents/Brumhack2015/Untitled-Fighting-Game-With-Clarifai/Images/backgrounds')

	try:
		shutil.copy(os.cwd()+'/'+ name, dest + '/backgrounds')
	except:
		pwd = os.getcwd()
		backs = os.listdir(pwd)
		name = backs[random.randint(0,len(backs))]
		shutil.copy(pwd +'/'+ name, dest+'/backgrounds')
		print '/!\\ WARNING! /!\\ NO IMAGE FOUND!\nGENERATING RANDOM BATTLEFIELD'
