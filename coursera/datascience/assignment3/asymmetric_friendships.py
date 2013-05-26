import MapReduce
import sys

"""
MapReduce Problem 4 - find asymmetric Friendships
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    personA = record[0]
    personB = record[1]
    
    mr.emit_intermediate(personA, personB)
    mr.emit_intermediate(personB, personA)

def reducer(key, list_of_values):
    for person in list_of_values:
        if list_of_values.count(person) == 1:
            mr.emit((key, person))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
