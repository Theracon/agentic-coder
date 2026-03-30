from functions.get_files_info import get_files_info

test_cases = [
    ("calculator", "."),
    ("calculator", "pkg"),
    ("calculator", "/bin"),
    ("calculator", "../"),
]

for test in test_cases:
    working_directory = test[0]
    directory = test[1]
    dir_view = "current" if directory == "." else f"'{directory}'"
    result = get_files_info(working_directory, directory)
    print(f"Result for {dir_view} directory:")
    print(result)
