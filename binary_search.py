import math
from evaluate_tests import evaluate_tests

def binary_search(l: list, searching_for):
    if len(l) == 0:
        print("List is empty")
        return

    index = int(len(l) / 2) + 1
    step = 1

    while l[index] != searching_for:
        direction = 1 if l[index] < searching_for else -1

        index = index + math.ceil(index / 2**step) * direction
        index = min(index, len(l) - 1)

        if step >= math.log(len(l), 2) + 1:
            print("Value is not in the provided list")
            return

        step += 1

    return index

tests = [{
    "input": {
        "l": [i for i in range(33)],
        "searching_for": 20
    },
    "output": 20
    },
    {
    "input": {
        "l": [0, 0, 0, 1, 2, 3, 15, 16, 20, 30, 50, 60, 61, 88, 89, 130, 133, 134, 145],
        "searching_for": 3
    },
    "output": 5
    },
    {
    "input": {
        "l": [],
        "searching_for": 3
    },
    "output": None
}]

evaluate_tests(binary_search, tests)
