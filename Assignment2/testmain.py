import twitpicapi
import psutil
import os


consumer_key=''
consumer_secret=''
access_token_key=''
access_token_secret=''
json_key = ''

def test(screenname,num):
	t = twitpicapi.TwitpicAPI(consumer_key, consumer_secret, access_token_key, access_token_secret, json_key)
	tags = t.Aggregate(screenname, num, "", 
	"", "")
	process = psutil.Process(os.getpid())
	print(process.memory_info().rss)
	return tags