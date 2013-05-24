import sys
import json

def getStates ():
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
        }
    return states

def getDict(afinnfile):
    #afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores

def sentiment (text, scores):
    words = text.split()
    sentiment = 0
    for word in words:
        lWord = word.lower()
        if lWord in scores:
            sentiment += scores[lWord]
    return sentiment

def addToDict (dic, key, val):
    if key in dic:
        dic[key] += val
    else:
        dic[key] = val

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = getDict (sent_file)
    
    #map from abbreviation to state and vise versa
    abbrToState = getStates()
    abbrToScore = {}
    
    for line in tweet_file:
        try:
            data = json.loads(line)
            userLoc = data["user"]["location"]
            placeLoc = data["place"]["full_name"]
            combinedLoc = userLoc +" "+ placeLoc
            #for every state:
            sentimentScore = sentiment(data["text"], scores)
            for state in abbrToState: #for every state
                if state in combinedLoc or abbrToState[state] in combinedLoc:
                    addToDict (abbrToScore, state, sentimentScore)
        except:
            pass

    highest = -10000
    happy = ""
    for state in abbrToScore:
        if abbrToScore[state] > highest:
            happy = state
            highest = abbrToScore[state]
    print happy

main()
