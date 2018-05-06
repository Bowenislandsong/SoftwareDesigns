from PIL import Image
import glob
import os
from subprocess import Popen, PIPE


from PIL import ImageFont
from PIL import ImageDraw 


def jpg2mp4():
	p = Popen(['ffmpeg', '-y', '-f', 'image2pipe', '-vcodec', 'mjpeg', '-r', '24', '-i', '-', '-vcodec', 'mpeg4', '-qscale', '5', '-r', '24', 'video.mp4'], stdin=PIPE)
	#for i in range(fps * duration):
	size = [400,400]
	for infile in glob.glob("*.jpg"):
		file, ext = os.path.splitext(infile)
		im = Image.open(infile)
		im.resize(size, resample=0)
	#    im = Image.new("RGB", (300, 300), (i, 1, 1))
		im.save(p.stdin, 'JPEG')
	p.stdin.close()
	p.wait()

def rmAllType():
	os.remove(os.path.join(os.path.dirname(__file__),
    '*.jpg'))

def rmPWDImg():
	filelist = glob.glob(os.path.join(os.getcwd(), '*.jpg'))
	for f in filelist:
		os.remove(f)

def labelonImage(text,filename):
	img = Image.open(filename)
	img = img.convert('RGB') # handel grey scale image error
	draw = ImageDraw.Draw(img)
	# font = ImageFont.truetype(<font-file>, <font-size>)
	width, height = img.size
	fnt = ImageFont.truetype('FreeMono.ttf', 40)
	#print (int(width*0.003* height*0.007))
	# draw.text((x, y),"Sample Text",(r,g,b))
	#print "expect string here and we got: "+str(text)
	## print test
	# print(text[:5])
	# print('\n')
	draw.text((width*0.3, height*0.7),' '.join(text),(0,0,0),font = fnt)
	img.save(filename)
	return text







