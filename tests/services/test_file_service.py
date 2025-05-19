import pytest

from application.domain.services.file_service import clear_file, save_data_to_file


@pytest.fixture
def test_file(tmp_path):
    file_path = tmp_path / "test_file.txt"
    yield file_path

    if file_path.exists():
        file_path.unlink()


def test_clear_file(test_file):
    with open(test_file, "w") as f:
        f.write("Some content")

    clear_file(test_file)

    with open(test_file, "r") as f:
        content = f.read()
    assert content == ""


def test_save_data_to_file(test_file):
    data = ["line1", "line2", "line3"]

    save_data_to_file(data, test_file)

    with open(test_file, "r") as f:
        content = f.readlines()
    assert content == [f"{item}\n" for item in data]


def test_save_data_to_file_append(test_file):
    data1 = ["line1", "line2"]
    data2 = ["line3", "line4"]

    save_data_to_file(data1, test_file)

    save_data_to_file(data2, test_file)

    with open(test_file, "r") as f:
        content = f.readlines()
    assert content == [f"{item}\n" for item in data1 + data2]
