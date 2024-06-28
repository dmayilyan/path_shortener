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


def test_create_placeholder_list(path_only_list):
    expected = [[chr(0)], [chr(0)], [chr(0)]]
    assert create_placeholder_list(path_only_list) == expected


def test_process_paths(path_only_list):
    expected = [
        "...s-client-bavo-protocol-manual-lhc-mellinbright-catmetrics/to/somewhere/far/far/away",
        "...s-client-bavo-task-script-lhc-plate-reader-echo-catmetrics/to/somewhere/far/far/away",
        "...s-task-script-hello-world/",
    ]
    assert process_paths(path_only_list) == expected
