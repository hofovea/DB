import sys

import MapReduce


mr = MapReduce.MapReduce()


def mapper(record):
    sequenceId = record[0]
    nucleotides = record[1]
    mr.emit_intermediate(nucleotides[0:-10], sequenceId)


def reducer(key, list_of_values):
    mr.emit(key)


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
