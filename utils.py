from config import CMD_TO_EXECUTE
from typing import Generator

def read_file(file_name:str) -> Generator:
    with open(file_name) as file:
        for line in file:
            yield line


def perform_action(cmd: str, value: str, data: Generator) -> Generator:
    return CMD_TO_EXECUTE[cmd](value=value, data=data)
