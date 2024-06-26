from itertools import zip_longest
from collections import deque
from os import path
from typing import Iterable, Tuple, List


# Terrimble ideas to make list object not to refer one
class EmptyString:
    """This class is made to enforce the list of empty string to
    have different objects"""

    def __str__(self):
        return ""


class EmptyList:
    """This class is made to enforce the list of empty string to
    have different objects"""

    def __str__(self):
        return []


def split_paths(paths: Iterable[str]) -> Tuple[List[str], Tuple[str]]:
    split_blocks = [path.split(p) for p in paths]

    paths, files = zip(*((p, f) for p, f in split_blocks))
    paths = [i.split("/") for i in paths]

    return paths, files


# Due to empty list creation pecularity we would stick to only list of lists
# object
def create_final_list(paths, fill_value=None) -> List[str]:
    if fill_value is None:
        fill_value = []

    # this si the only way that enforces lists inside not to be assigned to the same object
    return [[chr(0)] for _ in range(len(paths))]


def process_paths(paths, final_list):
    for slice_list in zip_longest(*paths, fillvalue=""):
        if all(map(lambda x: x < 10, map(len, slice_list))):
            for pathi, p in enumerate(slice_list):
                final_list[pathi].append(p)
            continue

        max_in_slice = max(map(len, slice_list))
        slice_list = [i.ljust(max_in_slice, chr(0)) for i in slice_list]

        mask = []
        for vals in zip(*slice_list):
            if len(set(vals)) != 1:
                mask.append(True)
            else:
                mask.append(False)

        surround_size = 2

        mask_shifted = mask.copy()
        mask_shifted += [False] * surround_size
        mask_shifted = mask_shifted[surround_size:]
        final_mask = [a or b for a, b in zip(mask, mask_shifted)]

        buffer_list = create_final_list(slice_list, fill_value=[])
        for vals in zip(*slice_list, final_mask):
            chars, match = vals[:-1], vals[-1]
            if len(set(chars)) == 1 and not match:
                for vali in range(len(chars)):
                    if buffer_list[vali][-1] != "...":
                        buffer_list[vali].append("...")
            else:
                for valj in range(len(chars)):
                    buffer_list[valj].append(vals[valj].strip(chr(0)))

        buffer_list = ["".join(bitem) for bitem in buffer_list]
        buffer_list = [bitem.strip(chr(0)) for bitem in buffer_list]

        for bi, fi in zip(buffer_list, final_list):
            fi.append(bi)

    final_list = [fi[1:] for fi in final_list]
    final_list = [path.join(*fi) for fi in final_list]

    return final_list


if __name__ == "__main__":
    a = "ns-client-bavo-protocol-manual-lhc-mellinbright-catmetrics/to/somewhere/far/far/away/foo.bar"
    b = "ns-client-bavo-task-script-lhc-plate-reader-echo-catmetrics/to/somewhere/far/far/away/notfoo.bar"
    c = "ns-task-script-hello-world/Lab1"

    path_list = [a, b]
    paths, filenames = split_paths(path_list)

    # TODO
    d = deque()

    final_list = create_final_list(paths)

    processed_paths = process_paths(paths, final_list)

    print(processed_paths)
