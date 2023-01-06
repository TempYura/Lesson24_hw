from config import CMD_TO_EXECUTE


def read_file(file_name):
    with open(file_name) as file:
        for line in file:
            yield line


def perform_action(cmd, value, data):
    return CMD_TO_EXECUTE[cmd](value=value, data=data)
