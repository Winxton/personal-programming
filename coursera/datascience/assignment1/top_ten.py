import sys
import json

def main ():
    tweet_file = open(sys.argv[1])
    topTen = []
    hashtagFreq = {}
    count = 0
    for line in tweet_file:
        try:
            data = json.loads(line)
            try:
                for tag in data["entities"]["hashtags"]:
                    count +=1 
                    hashtag = tag["text"]
                    #print hashtag
                    if hashtag in hashtagFreq:
                        hashtagFreq[hashtag] += 1
                    else :
                        hashtagFreq[hashtag] = 1

                    if hashtag not in topTen:
                        if len(topTen) < 10:
                            topTen.append(hashtag)
                        else:
                            updateTopTen(topTen, hashtagFreq, hashtag)
            except:
                pass
        except:
            pass

    
    for hashtag in topTen:
        print hashtag, float(hashtagFreq[hashtag])
    """
    print "-------DICT----------"
    htlist = sorted(hashtagFreq, key=hashtagFreq.get)
    listTen = htlist[-10:]
    for item in listTen:
        print item, hashtagFreq[item]
    print count
    """

def updateTopTen(topten, hashtagFreq, hashtag):
    low = hashtagFreq[topten[0]] #lowest freq
    idx = 0 #index of lowest
    for i in range (1, len(topten)):
        temptag = topten[i]
        if hashtagFreq[temptag] < low:
            idx = i
            low = hashtagFreq[temptag]

    if hashtagFreq[hashtag] > hashtagFreq[topten[idx]]:
        del topten[idx]
        topten.append(hashtag)

main()
