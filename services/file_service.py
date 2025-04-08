def clear_file(file_name: str) -> None:
    with open(f"{file_name}", "w") as file:
        pass


def save_data_to_file(data, file_name: str) -> None:
    with open(f"{file_name}", "a") as file:
        file.write(f"{data!r}\n")

    print(f"Output has been appended to {file_name}")
