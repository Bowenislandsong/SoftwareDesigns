#!/usr/bin/env python3
import sys
sys.path.insert(0, "../../Assignment1/")
import twmager
import img2video
import vision
import json
import mogoLog as lg
import trend
import glob




with open('twittersecrete.json') as secret:
	Tsecret = json.load(secret)

# allow user to choose what video content is
# Have google vision scan all the pictures for those contents
# resizeable video, allow passing size and time
# allow users to scan all the friends
twmager.twitter_api(Tsecret['Consumer_Key'], Tsecret['Consumer_Secret'],Tsecret['Access_Token'], Tsecret['Access_Token_Secret'])

twmager.download_tw_img("etcwilde")
# 

cli = lg.loguser("mongodb://localhost:27017","etcwilde")
# client.drop_database('<DBNAME>')

for infile in glob.glob("*.jpg"):
	lab= vision.labels(infile,'')
	if (lab != False):
		text = img2video.labelonImage(lab,infile)
		for t in text:
			lg.loginterests(t)

list = g.checktop(5)

lg.uploadlog()


img2video.jpg2mp4()

img2video.rmPWDImg()

trend.compare(list)
