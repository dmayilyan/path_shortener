from main import *
from pytest import fixture


@fixture
def path_list():
    a = "ns-client-bavo-protocol-manual-lhc-mellinbright-catmetrics/to/somewhere/far/far/away/foo.bar"
    b = "ns-client-bavo-task-script-lhc-plate-reader-echo-catmetrics/to/somewhere/far/far/away/notfoo.bar"
    c = "ns-task-script-hello-world/Lab1"

    return [a, b, c]


def test_split_files(path_list):
    expected = (
        (
            "ns-client-bavo-protocol-manual-lhc-mellinbright-catmetrics/to/somewhere/far/far/away",
            "ns-client-bavo-task-script-lhc-plate-reader-echo-catmetrics/to/somewhere/far/far/away",
            "ns-task-script-hello-world",
        ),
        ("foo.bar", "notfoo.bar", "Lab1"),
    )
    assert split_files(path_list) == expected


def test_create_final_paths(path_list):
    expected = len(path_list) * [""]
    assert create_final_list(path_list) == expected
