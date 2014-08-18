import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    record_type = record[0]
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
    orders = []
    line_items = []
    for v in list_of_values:
      record_type = v[0]
      if record_type == 'order':
        orders.append(v)
      elif record_type == 'line_item':
        line_items.append(v)

    for order in orders:
      for line_item in line_items:
        return_result = order + line_item
        mr.emit(return_result)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
