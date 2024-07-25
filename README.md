# Goal

Shorten paths so that they can fit on the screen.

# Expectations

It works for any count of paths and returns common parts replaced with `...` minus a windows of size given as a parameter. In simpler terms, you can expect common chars present aroung `...` equal to a given window size (1 by default)

For example for a list of 2 paths with same begining and end we will get:

```
This:
['ns-client-bavo-protocol-manual-lhc-mellinbright-catmetrics/to/somewhere/far/far/away/foo.bar', 'ns-client-bavo-task-script-lhc-plate-reader-echo-catmetrics/to/somewhere/far/far/away/notfoo.bar']
Becomes this:
['...-protocol-manual-lhc-mellinbright-.../to/somewhere/far/far/away/foo.bar', '...-task-script-lh-plate-reader-echo-.../to/somewhere/far/far/away/notfoo.bar']
```
