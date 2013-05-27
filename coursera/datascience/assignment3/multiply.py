import MapReduce
import sys

"""
MapReduce problem 6: Matrix Multiplication
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# A is L x M
# B is M x N
# matrix dimensions hardcoded in 
L = 4
N = 4

def mapper(record):
    matrix = record[0]
    i = record[1]
    j = record[2]
    val = record[3]
    if 'a' == matrix:
        for k in range(0,L+1):
            mr.emit_intermediate((i,k),(j,val))
    if 'b' == matrix:
        for k in range(0,N+1):
            mr.emit_intermediate((k,j),(i,val))

def reducer(key, list_of_values):
    key_vals = {}
    for val in list_of_values:
        if val[0] not in key_vals:
            key_vals[val[0]] = [val[1]]
        else:
            key_vals[val[0]].append(val[1])

    sum = 0
    for idx in key_vals:
        if len(key_vals[idx]) == 2:
            sum += key_vals[idx][0] * key_vals[idx][1]
    print sum
    
# Do not modify below this line
# =============================

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)

