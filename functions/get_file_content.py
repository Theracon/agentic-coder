import os

from google.genai import types

from config import MAX_CHAR_COUNT


def get_file_content(working_directory, file_path):
    try:
        abs_wd = os.path.abspath(working_directory)
        td = os.path.normpath(os.path.join(abs_wd, file_path))
        is_td_valid = os.path.commonpath([abs_wd, td]) == abs_wd
        if not is_td_valid:
            return f'Error [get_file_content]: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(td):
            return f'Error [get_file_content]: File not found or is not a regular file: "{file_path}"'
        contents = ""
        with open(td, "r") as file:
            contents = file.read(MAX_CHAR_COUNT)
            if file.read():
                contents += (
                    f'[...File "{file_path}" truncated at {MAX_CHAR_COUNT} characters]'
                )
            return contents
    except Exception as e:
        return f"Error [get_file_content]: An unknown error occurred -> {e}"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Fetches the content of a file in a specified file_path",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to read from",
            ),
        },
        required=["file_path"],
    ),
)
