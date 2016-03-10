from clarifai.client import ClarifaiApi
import json
import os
clarifai_api = ClarifaiApi()

def getTags(filename, returndir):
	print "Getting tags for " + filename
	currentfile = open(filename)
	result = clarifai_api.tag_images(currentfile)
	currentfile.close()
	tag = result["results"][0]["result"]["tag"]["classes"]
	prob = result["results"][0]["result"]["tag"]["probs"]
	
	if not os.path.exists(returndir):
		os.makedirs(returndir)
	returnfile = open(returndir + filename + '.py', 'w')

	tags = {}
	for i in range(0, len(tag)):	
		tags[tag[i]] = str(prob[i])
	json.dump(tags, returnfile)
	returnfile.close()

folders = ['heads','torsos','legs','backgrounds']

for folder in folders:
	output = '/home/arthur/Documents/Brumhack2015/Untitled-Fighting-Game-With-Clarifai/Tags/' + folder + '/'
	os.chdir('/home/arthur/Documents/Brumhack2015/Untitled-Fighting-Game-With-Clarifai/Images/'+folder)
	pwd = os.getcwd()

	pics = os.listdir(pwd)
	pics.sort()

	for pic in pics:
		getTags(pic, output)
