from functions.run_python_file import run_python_file

test_cases = [
    ("calculator", "main.py"),
    ("calculator", "main.py", ["3 + 5"]),
    ("calculator", "tests.py"),
    ("calculator", "../main.py"),
    ("calculator", "nonexistent.py"),
    ("calculator", "lorem.txt"),
]

for test in test_cases:
    args = None
    if len(test) > 2:
        args = test[2]
    if args:
        result = run_python_file(test[0], test[1], args)
    else:
        result = run_python_file(test[0], test[1])
    print(result)
