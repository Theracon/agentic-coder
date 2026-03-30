import os

from google.genai import types


def get_files_info(working_directory, directory="."):
    try:
        abs_wd = os.path.abspath(working_directory)
        td = os.path.normpath(os.path.join(abs_wd, directory))
        is_td_valid = os.path.commonpath([abs_wd, td]) == abs_wd
        if not is_td_valid:
            return f'Error [get_files_info]: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(td):
            return f'Error [get_files_info]: "{directory}" is not a directory'
        contents = os.listdir(td)
        formatted_contents = [
            format(
                content,
                os.path.getsize(os.path.normpath(os.path.join(td, content))),
                os.path.isdir(os.path.normpath(os.path.join(td, content))),
            )
            for content in contents
        ]
        stringified_content = "\n".join(formatted_contents)
        return stringified_content
    except Exception as e:
        return f"Error [get_files_info]: An unknown error occurred -> {e}"


def format(name, size, is_dir):
    return f"- {name}: file_size={size} bytes, is_dir={is_dir}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)
