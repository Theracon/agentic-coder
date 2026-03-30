from functions.get_file_content import get_file_content

test_cases = [
    ("calculator", "lorem.txt"),
    ("calculator", "main.py"),
    ("calculator", "pkg/calculator.py"),
    ("calculator", "/bin/cat"),
    ("calculator", "pkg/does_not_exist.py"),
]

for test in test_cases:
    working_directory = test[0]
    filepath = test[1]
    result = get_file_content(working_directory, filepath)
    print(f"Result from {filepath}:")
    print(result[:10000])
    print(len(result))
