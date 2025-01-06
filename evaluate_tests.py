import timeit


def evaluate_tests(func, tests: list[dict]):
    for test in tests:
        output = func(**test['input'])
        exec_time = round(timeit.timeit(lambda: func(**test['input']), number=1000), 5)



        print(f"Input: {test}")
        print(f"Expected output: {test['output']}")
        print(f"Actual output: {output}")
        print(f"Execution time: {exec_time} ms")
        print(f"Test result: {'PASSED' if output == test['output'] else 'FAILED'}\n\n")
