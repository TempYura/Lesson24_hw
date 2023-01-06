import re
from typing import Generator, Pattern

def filter_query(value: str, data: Generator) -> Generator:
    return (x for x in data if value in x)


def map_query(value: str, data: Generator) -> Generator:
    col_number: int = int(value)
    return (x for x in map(lambda x: x.split(' ')[col_number], data))


def unique_query(value: str, data: Generator) -> Generator:
    return (x for x in set(data))


def sort_query(value: str, data: Generator) -> Generator:
    reverse: bool = value == "desc"
    return (x for x in sorted(data, reverse=reverse))


def limit_query(value: str, data: Generator) -> Generator:
    limit: int = int(value)
    return (x for x, _ in zip(data, range(limit)))


def regex_query(value: str, data: Generator) -> Generator:
    reg: Pattern = re.compile(value)
    return (line for line in data if reg.search(line))
