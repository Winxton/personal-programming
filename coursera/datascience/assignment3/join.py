import MapReduce
import sys

"""
MapReduce Problem 2: Relational Join
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order_id
    # value: other columns in table
    order_id  = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
    # key: order_id
    # value: list of (column list)
    columns = []
    for val in list_of_values:
        if (val[0] == "order"):
            for test_val in list_of_values:
                if test_val[0] == "line_item":
                    mr.emit(val + test_val)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
