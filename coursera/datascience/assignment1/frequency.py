import json
import sys

def main():
	tweet_file = open (sys.argv[1])
	freqMap = {}
	tot = 0

	for line in tweet_file:
		try:	

			data = json.loads(line)
			text = data["text"]
			tokens = text.split()
			for token in tokens:
				tot += 1
				if token in freqMap:
					freqMap[token] += 1
				else :
					freqMap[token] = 1
		except:
			pass

	for key, value in freqMap.iteritems() :
		print key, '{0:.10f}'.format(float(value)/tot)

main()
