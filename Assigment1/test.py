import twmager
import img2video
import vision

import glob

# allow user to choose what video content is
# Have google vision scan all the pictures for those contents
# resizeable video, allow passing size and time
# allow users to scan all the friends

Imager.twitter_api('consumer_token',"consumer_secret","key","secret")

twmager.download_tw_img("etcwilde")
# 

# img2video.rmAllType()

for infile in glob.glob("*.jpg"):
	lab= vision.labels(infile,'')
	if (lab != False):
		img2video.labelonImage(lab,infile)

img2video.jpg2mp4()