import json

def main():
    f = open("data/records.json")
    num = 0
    for dataline in f:
        if num < 5:
            data = json.loads(dataline, encoding='latin-1')
            num += 1
            print data[1]
            print data[0:1] + data[2:10]

if __name__ == '__main__':
    main()
