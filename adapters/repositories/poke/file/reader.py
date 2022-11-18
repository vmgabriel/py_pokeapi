"""Reader of CSV"""

# Libraries
import csv
from typing import Any, Callable
from pathlib import Path
from functools import lru_cache
from dataclasses import dataclass


@dataclass
class CsvData:
    headers: list[str]
    contents: list[list[Any]]


def read_fixture(filename: str | Path) -> CsvData:
    """Read Fixture content of filename and generate CSVData or Error"""
    csv_reader = CsvData(headers=[], contents=[])
    with open(filename, mode="r") as f:
        [headers, *contents] = list(csv.reader(f))
        csv_reader.headers = headers
        csv_reader.contents = contents
    return csv_reader


@lru_cache
def return_type(struct: str) -> list[Callable]:
    def return_callable(type: str) -> Callable:
        match type:
            case "int":
                return lambda x: int(x)
            case _:
                return lambda x: x

    return [return_callable(ref_type) for ref_type in struct.split(",")]


def to_struct(data: list[Any], struct: str) -> list[Any]:
    """Define to structure"""
    return [call(val) for val, call in zip(data, return_type(struct))]


def define_structure(csv_data: CsvData, struct: str) -> CsvData:
    """based into string convert data"""
    csv_data.contents = [to_struct(x, struct) for x in csv_data.contents]
    return csv_data


__all__ = [
    read_fixture,
    define_structure,
    CsvData
]
