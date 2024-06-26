from main import *
from pytest import fixture, mark


@fixture
def path_list():
    a = (
        "ns-client-bavo-protocol-manual-lhc-mellinbright-catmetrics/to/"
        "somewhere/far/far/away/foo.bar"
    )
    b = (
        "ns-client-bavo-task-script-lhc-plate-reader-echo-catmetrics/to/"
        "somewhere/far/far/away/notfoo.bar"
    )
    c = "ns-task-script-hello-world/Lab1"

    return [a, b, c]


@fixture
def path_only_list():
    a = [
        "ns-client-bavo-protocol-manual-lhc-mellinbright-catmetrics",
        "to",
        "somewhere",
        "far",
        "far",
        "away",
    ]
    b = [
        "ns-client-bavo-task-script-lhc-plate-reader-echo-catmetrics",
        "to",
        "somewhere",
        "far",
        "far",
        "away",
    ]
    c = ["ns-task-script-hello-world"]

    return [a, b, c]


def test_split_paths(path_list, path_only_list):
    expected = (
        path_only_list,
        ("foo.bar", "notfoo.bar", "Lab1"),
    )
    assert split_paths(path_list) == expected


@mark.parametrize(
    "fill_value, expected",
    [([], [[], [], []]), ("", ["", "", ""])],
)
def test_create_final_paths(path_list, fill_value, expected):
    assert create_final_list(path_list, fill_value) == expected


def test_create_paths_slice(path_list): ...
