import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    person_A = record[0]
    person_B = record[1]
    #person B is a friend of person A
    mr.emit_intermediate(person_A, 1)

def reducer(key, list_of_values):
    #key: person
    #value: 1 for each friend
    total = 0
    for v in list_of_values:
      total += v
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
