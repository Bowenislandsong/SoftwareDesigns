from PIL import Image
import glob
import os
from subprocess import Popen, PIPE

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

