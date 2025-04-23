import logging


def clear_file(file_name: str) -> None:
    logging.info(f"Clearing file: {file_name}")
    with open(f"{file_name}", "w") as file:
        pass


def save_data_to_file(data, file_name: str) -> None:
    with open(f"{file_name}", "a") as file:
        for item in data:
            file.write(f"{item!s}\n")

    logging.info(f"Output has been appended to {file_name}")


def save_most_ordered_to_file(data, file_name: str) -> None:
    with open(file_name, "w") as file:
        file.write(f"{str(data)}")

    print("Output has been saved to most_ordered_output.txt")
