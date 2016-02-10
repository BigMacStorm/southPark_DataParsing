import time
import re

def remove_trash(sent):
	ret = ''
	flag1c = 0
	flag2c = 0
	for i in sent:
		if i == '[':
			flag1c += 1
		elif i == '<':
			flag2c += 1
		elif i == ']' and flag1c > 0:
			flag1c -= 1
		elif i == '>'and flag2c > 0:
			flag2c -= 1
		elif flag1c == 0 and flag2c == 0:
			ret += i
	return ret

def parseEpisode(episodeNumber):
	fileObject = open('scripts/' + str(episodeNumber),'r')
	count = 2
	flag = False
	name = False
	currentSpeaker = ""
	for x in fileObject:
		x = remove_trash(x)
		x = x.replace(".", " ")
		x = x.replace("?", "")
		x = x.replace("!", "")
		x = x.replace(",", "")
		x = x.replace(";", "")
		x = x.replace("\"", "")
		x = x.upper()
		wordList = x.split()

		if(wordList == []):
			continue

		if(wordList == ['&#160']):
			print "Done parsing this script"
			break

		#this first part here is just to find the start
		if(wordList == ['SCRIPT']):
			count -= 1
			if(count == 0):
				print "Found start of script, starting to print!"
				flag = True
				continue
		if(not flag or count != 0):
			continue

		#means the script has started.
		time.sleep(0.25)
		print wordList
		if(not name):
			name = True
			currentSpeaker = wordList[0]
			currentSpeaker = currentSpeaker.replace(":", "")
			break
		else:
			#some magic here


parseEpisode(2)