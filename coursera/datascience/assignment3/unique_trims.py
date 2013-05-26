import MapReduce
import sys

"""
MapReduce Problem 5 - Unique Trimmed DNA Sequences
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    sequence_id = record[0]
    nucleotides = record[1]
    
    mr.emit_intermediate(nucleotides[:-10], sequence_id)

def reducer(key, list_of_values):
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
