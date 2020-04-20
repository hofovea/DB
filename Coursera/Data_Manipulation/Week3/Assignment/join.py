import sys

import MapReduce


mr = MapReduce.MapReduce()


def mapper(record):
    order_id = record[1]

    mr.emit_intermediate(order_id, record)


def mapper(record):
    identifier = record[1]

    mr.emit_intermediate(identifier, record)


def reducer(key, list_of_values):
    order = []
    for value in list_of_values:
        if value[0] == 'order':
            order = value
        else:
            merged = order + value
            mr.emit(merged)


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
