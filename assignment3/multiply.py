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
    matrix = record[0]
    i = record[1]
    j = record[2]
    val = record[3]

    if matrix == 'a':
      for x in [0,1,2,3,4]:
        mr.emit_intermediate(str(i) + str(x), [j, val])
    
    if matrix == 'b':
      for x in [0,1,2,3,4]:
        mr.emit_intermediate(str(x) + str(j), [i, val])

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    i = int(key[0])
    j = int(key[1])

    value_dict = {}
    for v in list_of_values:
      if value_dict.get(v[0]) == None:
        value_dict[v[0]] = [v[1]]
      else:
        value_dict[v[0]].append(v[1])

    total = 0
    for pos, values in value_dict.items():
      if len(values) == 2:
        total += values[0] * values[1]

    mr.emit((i, j, total))
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
