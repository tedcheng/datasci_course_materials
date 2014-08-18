import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    trim = value[0:-10]
    
    mr.emit_intermediate(trim, trim)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts

    mr.emit(list_of_values[0])

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
