import sys
import json


class ScoreWeight:
    def __init__ (self, score, weight):
        self.score = score;
        self.weight = weight

def getDict(afinnfile):
    #afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores

def get_sentiment (text, scores, unknownScores):
    words = text.split()
    sentiment = 0
    for word in words:
        lWord = word.lower()
        if lWord in scores:
            sentiment += scores[lWord]
        if word in unknownScores:
            sentiment += unknownScores[word].score
    return sentiment

def get_count (text, scores, unknownScores):
    count = 1
    words = text.split()
    for word in words:
        if word.lower() in scores or word in unknownScores:
            count += 1
    return count

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = getDict (sent_file)
    
    unknownScores = {}
    for line in tweet_file:
        try:
            text = json.loads(line)["text"]
            sentiment = get_sentiment(text,scores,unknownScores)
#calculate sentiment of unknown words
            words = text.split()
            numWords = get_count (text, scores, unknownScores)#= len(words)
            for word in words:
                if word not in scores:
                    average = float(sentiment) / numWords
                    if word in unknownScores:
                        unknownScores[word].score  = unknownScores[word].weight * unknownScores[word].score + average
                        unknownScores[word].weight += 1
                        unknownScores[word].score  = float(unknownScores[word].score) / (unknownScores[word].weight)
                    else:
                        sw = ScoreWeight(average, 1)
                        unknownScores[word] = sw
        except:
            pass

    for unknown in unknownScores:
        try:
            print unknown, unknownScores[unknown].score
        except:
            pass

main()
    
