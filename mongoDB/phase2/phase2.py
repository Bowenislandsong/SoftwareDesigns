#!/usr/bin/env python2
import sys
sys.path.insert(0, "../../Assignment1/")
import twmager
import img2video
import vision
import json

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

for infile in glob.glob("*.jpg"):
	lab= vision.labels(infile,'')
	if (lab != False):
		img2video.labelonImage(lab,infile)

img2video.jpg2mp4()

img2video.rmPWDImg()