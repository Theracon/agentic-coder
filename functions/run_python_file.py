import os
import subprocess

from google.genai import types


def run_python_file(working_directory, file_path, args=None):
    try:
        abs_wd = os.path.abspath(working_directory)
        td = os.path.normpath(os.path.join(abs_wd, file_path))
        is_td_valid = os.path.commonpath([abs_wd, td]) == abs_wd
        if not is_td_valid:
            return f'Error [run_python_file]: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(td):
            return f'Error [run_python_file]: "{file_path}" does not exist or is not a regular file'
        if not td.endswith(".py"):
            return f'Error [run_python_file]: "{file_path}" is not a Python file'
        command = ["python", td]
        if args is not None:
            command.extend(args)
        cwd = "/".join(td.split("/")[:-1])
        result = subprocess.run(
            command, cwd=cwd, text=True, timeout=30, capture_output=True
        )
        output = ""
        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}. "
        if not result.stdout or not result.stderr:
            output += "No output produced. "
        if result.stdout:
            output += f"STDOUT: {result.stdout}"
        if result.stderr:
            output += f"STDERR: {result.stderr}"
        return output
    except Exception as e:
        return f"Error [run_python_file]: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run a python file at a specified file_path",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the python executable file to run",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="A list of string arguments to pass to the python executable file",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
        required=["file_path"],
    ),
)
