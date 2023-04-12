import json

from pip._internal import operations


def get_json(file_name):
    with open("operations.json", "wr") as f:
        operations = json.load(f)
    """Чтение файла JSON и возвращение объекта Python"""
    return operations



def get_operations_last_five():
    for operation in get_operations_last_five:
        if operation["EXECUTED"] == operation[0:5]:
            return operation
    # return None
print()









