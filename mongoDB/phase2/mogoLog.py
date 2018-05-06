#!/usr/bin/env python2
from pymongo import MongoClient
import sys
sys.path.insert(0, "../")
import phase1 as p1
import json

my_descriptors = {}
username = ""
cli = ''

def loguser(mongodb, _username):
    print("Connecting to Mongo...")
    global username 
    global cli
    username = _username
    cli =  MongoClient(mongodb)
    # db = "tweeter"
	# collec = username
    # return username


def uploadlog():
    global username
    global cli
    global my_descriptors
    collection = p1.getCollection(cli,"tweeterME",username)
    
    my_descriptors = json.dumps(my_descriptors)
    my_descriptors = json.loads(my_descriptors)
    print(type(my_descriptors))
    collection.insert_one(my_descriptors)
    tempdesc = my_descriptors
    my_descriptors = {}
    return tempdesc

def loginterests(descriptor):
    global my_descriptors
    if (descriptor in my_descriptors):
        my_descriptors[descriptor] = my_descriptors[descriptor]+1
    else:
        my_descriptors[descriptor] =1
        pass

def savetop(num):
    global my_descriptors
    keylst = my_descriptors.keys()
    vallist = my_descriptors.values()
    vallist.sort()
    try:
        if (len(keylst) > num):
            for key in keylst:
                print(key)
                print( vallist[0])
                if (my_descriptors.get(key) <= vallist[0]):
                    my_descriptors.pop(key, None)
                    savetop(num)
    except:
        print(len(keylst))
        print("Unexpected error:", sys.exc_info()[0])
        raise


# if __name__ == "__main__":
# 	'''
# 	This is a test for the functions above
# 	'''
#     mongodb  = "mongodb://localhost:27017"