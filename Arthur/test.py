import os
import json
import Image
from nltk.corpus import wordnet as wn
import random

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

def makePic(head, torso, legs):
	back = Image.new("RGB",(800,400), "white")
        backsize = back.size
	
	head.thumbnail((100,100))
	torso.thumbnail((100,100))
	legs.thumbnail((100,100))
	partsize = head.size[0]
	
        

        back.paste(legs, (backsize[0]/2 - partsize/2, backsize[1]-partsize), legs)
        back.paste(torso, (backsize[0]/2 - partsize/2, backsize[1]-2*partsize), torso)
        back.paste(head, (backsize[0]/2 - partsize/2, backsize[1]-3*partsize), head)

        return back



parts = ['heads','torsos','legs']
images = []
trollparts = 0
for part in parts:
	inptlist = raw_input("Enter single-word tags for the " + part + " as comma seperated list\n")
	inptlist = inptlist.replace(" ", "")
	words = inptlist.split(',')
	backgroundtags += words

	os.chdir('/home/arthur/Documents/Brumhack2015/Untitled-Fighting-Game-With-Clarifai/Tags/' + part)
	name = findBestMatch(words).replace(".py","")

	os.chdir('/home/arthur/Documents/Brumhack2015/Untitled-Fighting-Game-With-Clarifai/Images/' + part)

	try:
		img = Image.open(name)
	except:
		if(part=='heads'):
			img = Image.open('/home/arthur/Documents/Brumhack2015/Untitled-Fighting-Game-With-Clarifai/SPECIAL images/troll.png')
			summons = 'TROLL'
		elif(part=='torsos'):
			img = Image.open('/home/arthur/Documents/Brumhack2015/Untitled-Fighting-Game-With-Clarifai/SPECIAL images/totem.png')
			summons = 'POLE'
		else:
			img = Image.open('/home/arthur/Documents/Brumhack2015/Untitled-Fighting-Game-With-Clarifai/SPECIAL images/hole.png')
			summons = 'HOLE'

		trollparts+=1		
		print '/!\\ WARNING! /!\\ NO IMAGE FOUND!\nSUMMONING THE %s!' % (summons,)
	images.append(img)


endpic = makePic(images[0], images[1], images[2])
endpic.show()

for image in images:
	del image
del endpic

