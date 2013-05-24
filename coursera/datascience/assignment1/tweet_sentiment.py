import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def getDict(afinnfile):
    #afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores

#returns sentiment score given tweet
def sentiment(text, scores):
    words = text.split()
    sentiment = 0
    for word in words:
        lWord = word.lower()
        if lWord in scores:
            sentiment += scores[lWord]
    return sentiment

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2],"r")
    scores = getDict(sent_file) #Dictionary of scores
    for line in tweet_file:
        try :
            data = json.loads(line)
            text = data["text"]
            if "hashtags" in data:
                print data["hashtags"]
            num = sentiment(text,scores)
            print num
        except :
            print 0

if __name__ == '__main__':
    main()
