import sys

import MapReduce


mr = MapReduce.MapReduce()


def mapper(record):
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
        mr.emit_intermediate(w, key)


def reducer(key, list_of_values):
    unique_books = []
    for v in list_of_values:
        if v not in unique_books:
            unique_books.append(v)
    mr.emit((key, unique_books))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
