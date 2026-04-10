import pytest

def read_population_file(filename):
    data = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(",")

            if len(parts) != 3:
                continue

            country = parts[0].strip()
            area = float(parts[1].strip())
            population = int(parts[2].strip())

            data.append({
                "country": country,
                "area": area,
                "population": population
            })

    return data


def sort_by_area(data):
    return sorted(data, key=lambda x: x["area"])


def sort_by_population(data):
    return sorted(data, key=lambda x: x["population"])



@pytest.fixture
def sample_file(tmp_path):
    file = tmp_path / "data.txt"

    file.write_text(
        "Ukraine, 603628, 41000000\n"
        "Poland, 312696, 38000000\n"
        "Germany, 357022, 83000000\n",
        encoding="utf-8"
    )

    return file


# 🔹 TEST читання
def test_read_population_file(sample_file):
    data = read_population_file(sample_file)

    assert len(data) == 3
    assert data[0]["country"] == "Ukraine"



@pytest.mark.parametrize("expected_first", [
    "Poland",
])
def test_sort_by_area(sample_file, expected_first):
    data = read_population_file(sample_file)
    sorted_data = sort_by_area(data)

    assert sorted_data[0]["country"] == expected_first



@pytest.mark.parametrize("expected_last", [
    "Germany",
])
def test_sort_by_population(sample_file, expected_last):
    data = read_population_file(sample_file)
    sorted_data = sort_by_population(data)

    assert sorted_data[-1]["country"] == expected_last
