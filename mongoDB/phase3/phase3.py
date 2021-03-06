#!/usr/bin/env python3
import sys
sys.path.insert(0, "../../Assignment1/")
sys.path.insert(1, "../Phase2/")
import twmager
import img2video
import vision
import json
import mogoLog as lg
import glob
import compare

screenname = "etcwilde"
with open('twittersecrete.json') as secret:
	Tsecret = json.load(secret)

# allow user to choose what video content is
# Have google vision scan all the pictures for those contents
# resizeable video, allow passing size and time
# allow users to scan all the friends
twmager.twitter_api(Tsecret['Consumer_Key'], Tsecret['Consumer_Secret'],Tsecret['Access_Token'], Tsecret['Access_Token_Secret'])

twmager.download_tw_img(screenname)
# 

cli = lg.loguser("mongodb://localhost:27017",screenname)
# client.drop_database('<DBNAME>')

for infile in glob.glob("*.jpg"):
	lab= vision.labels(infile,'')
	if (lab != False):
		text = img2video.labelonImage(lab,infile)
		for t in text:
			lg.loginterests(t)

lg.savetop(20)


top5 = lg.uploadlog()


img2video.jpg2mp4()

img2video.rmPWDImg()

compare.showcompare(screenname,top5)
