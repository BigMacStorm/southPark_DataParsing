import time
import re
import json

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
	poem = False
	currentSpeaker = ""
	for x in fileObject:
		if( "<i>[End of" in x or "[<b>End" in x or "</td></tr></table>" in x):
			break
		if("poem" in x or poem):
			poem = True
			if("</div>" in x):
				poem = False
			continue
		x = remove_trash(x)
		x = x.replace(".", " ")
		x = x.replace("?", "")
		x = x.replace("!", "")
		x = x.replace(",", "")
		x = x.replace(";", "")
		x = x.replace("\"", "")
		x = x.replace(")", "")
		x = x.replace("(", "")
		x = x.upper()
		wordList = x.split()

		if(wordList == []):
			continue

		#this first part here is just to find the start
		if(wordList == ['SCRIPT']):
			count -= 1
			if(count == 0):
				flag = True
				continue
		if(not flag or count != 0):
			continue

		#means the script has started.
		#time.sleep(0.02)
		#print wordList
		if(not name):
			name = True
			currentSpeaker = x
			currentSpeaker = currentSpeaker.replace(":", "")
			currentSpeaker = currentSpeaker.replace("\n", "")
		else:
			if(currentSpeaker not in memory):
				memory[currentSpeaker] = {}
			for word in wordList:
				word = re.sub('[^\x00-\x7f]', '', word)
				if(word not in memory[currentSpeaker]):
					memory[currentSpeaker][word] = 1
				else:
					memory[currentSpeaker][word] += 1
			name = False

memory = {}
for number in range(1, 262):
	parseEpisode(number)
#print sorted(((v,k) for k,v in memory["CARTMAN"].iteritems()), reverse=True)
jsonString = json.dumps(memory)
print jsonString