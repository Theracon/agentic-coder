import os

from google.genai import types


def write_file(working_directory, file_path, content):
    try:
        abs_wd = os.path.abspath(working_directory)
        td = os.path.normpath(os.path.join(abs_wd, file_path))
        is_td_valid = os.path.commonpath([abs_wd, td]) == abs_wd
        if not is_td_valid:
            return f'Error [write_file]: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(td):
            return f'Error [write_file]: Cannot write to "{file_path}" as it is a directory'
        dir_path = os.path.dirname(td)
        if dir_path is not None:
            os.makedirs(dir_path, exist_ok=True)
        with open(td, "w") as file:
            file.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error [write_file]: An unknown error occurred -> {e}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write to a file at a specified file_path",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to write to",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to a specified file",
            ),
        },
        required=["file_path", "content"],
    ),
)
