import re


def filter_query(value, data):
    return (x for x in data if value in x)


def map_query(value, data):
    col_number = int(value)
    return map(lambda x: x.split(' ')[col_number], data)


def unique_query(value, data):
    return (x for x in set(data))


def sort_query(value, data):
    reverse = value == "desc"
    return (x for x in sorted(data, reverse=reverse))


def limit_query(value, data):
    limit = int(value)
    return (x for x, _ in zip(data, range(limit)))


def regex_query(value, data):
    reg = re.compile(value)
    return (line for line in data if reg.search(line))
