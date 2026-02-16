import os
from google.genai import types


def write_file(working_directory: str, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f"Error: {file_path} is not in the working directory"

    parent_directory = os.path.dirname(abs_file_path)
    if not os.path.isdir(parent_directory):
        try:
            os.makedirs(parent_directory)
        except Exception as e:
            return f"Could not create parent directory {parent_directory} \n {e}"

    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
            return f"successfully wrote to {file_path} {len(content)} characters"
    except Exception as e:
        return f"failed to write to file {abs_file_path} \n {e}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwrites and exiting file or writes to a new file if it doesn't exist (and create required parent dirs safely), constrained to the current working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The contents to write to the file as as string",
            ),
        },
        required=["file_path", "content"],
    ),
)
