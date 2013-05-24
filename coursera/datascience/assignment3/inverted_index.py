import MapReduce
import sys

mr = MapReduce.MapReduce()

# Map function
# mr - MapReduce object
# data - json object formatted as a string
def mapper(record):
    doc_id = record[0]
    for word in record[1].split():
        mr.emit_intermediate(word, doc_id)

# Reduce function
# mr - MapReduce object
# key - key generated from map phase, associated to list_of_values
# list_of_values - values generated from map phase, associated to key
def reducer(key, list_of_values):
    doc_list = []
    for doc in list_of_values:
        if doc not in doc_list:
            doc_list.append(doc)
    # output item (only for reducer)
    mr.emit((key, doc_list))

def main():
    # Assumes first argument is a file of json objects formatted as strings, 
    #one per line.
    mr.execute(open(sys.argv[1]), mapper, reducer)

if __name__ == '__main__':
    main()
