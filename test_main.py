from main import split_files

a = "ns-client-bavo-protocol-manual-lhc-mellinbright-catmetrics/to/somewhere/far/far/away/foo.bar"
b = "ns-client-bavo-task-script-lhc-plate-reader-echo-catmetrics/to/somewhere/far/far/away/notfoo.bar"
c = "ns-task-script-hello-world/Lab1"


def test_split_files():
    expected = (
        (
            "ns-client-bavo-protocol-manual-lhc-mellinbright-catmetrics/to/somewhere/far/far/away",
            "ns-client-bavo-task-script-lhc-plate-reader-echo-catmetrics/to/somewhere/far/far/away",
            "ns-task-script-hello-world",
        ),
        ("foo.bar", "notfoo.bar", "Lab1"),
    )
    assert split_files([a, b, c]) == expected
