from functions.run_python_file import run_python_file


def main():
    working_directory = "calculator"
    print(
        run_python_file(
            working_directory=working_directory, file_path="main.py", args=["3 + 5"]
        )
    )
    # print(run_python_file(working_directory=working_directory, file_path="test.py"))
    # print(run_python_file(working_directory=working_directory, file_path="../main.py"))
    # print(run_python_file(working_directory=working_directory, file_path="non_existent.py"))


if __name__ == "__main__":
    main()
