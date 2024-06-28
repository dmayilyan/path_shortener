from itertools import zip_longest
from os import path
from typing import Iterable, List, Tuple


def split_paths(paths: Iterable[str]) -> Tuple[List[str], Tuple[str]]:
    split_blocks = [path.split(p) for p in paths]

    paths, files = zip(*((p, f) for p, f in split_blocks))
    # This is not OS agnostic approach
    paths = [i.split("/") for i in paths]

    return paths, files


def create_placeholder_list(paths: List[List[str]]) -> List[List[str]]:
    """This is the only reasonalbe way to enforce lists inside of a list not
    to be assigned to the same object"""
    return [[chr(0)] for _ in range(len(paths))]


def create_mask(slice_list: List[str]) -> List[bool]:
    mask = []
    for vals in zip(*slice_list):
        if len(set(vals)) != 1:
            mask.append(True)
        else:
            mask.append(False)

    SURROUND_SIZE = 2

    mask_shifted = mask.copy()
    mask_shifted += [False] * SURROUND_SIZE
    mask_shifted = mask_shifted[SURROUND_SIZE:]

    return [a or b for a, b in zip(mask, mask_shifted)]


def split_slice(path_slice: List[str]) -> List[Tuple[str]]:
    # We use len freely as we know that path slices are
    # already of an equal size
    splits = [(i[: len(i) // 2], i[len(i) // 2:]) for i in path_slice]
    return [i for i in zip(*splits)]


def process_paths(paths: List[List[str]]) -> List[str]:
    MIN_FOLDER_LENGTH = 10
    final_list = create_placeholder_list(paths)
    for slice_list in zip_longest(*paths, fillvalue=""):
        if all(map(lambda x: x < MIN_FOLDER_LENGTH, map(len, slice_list))):
            for pathi, p in enumerate(slice_list):
                final_list[pathi].append(p)
            continue

        max_in_slice = max(map(len, slice_list))
        slice_list = [i.ljust(max_in_slice, chr(0)) for i in slice_list]

        # TODO
        first_half, second_half = split_slice(slice_list)
        mask = create_mask(slice_list)

        buffer_list = create_placeholder_list(slice_list)
        for vals in zip(*slice_list, mask):
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

    # Getting rid of the object uniquiness enforcer
    final_list = [fi[1:] for fi in final_list]
    final_list = [path.join(*fi) for fi in final_list]

    return final_list


if __name__ == "__main__":
    a = (
        "ns-client-bavo-protocol-manual-lhc-mellinbright-catmetrics/to/"
        "somewhere/far/far/away/foo.bar"
    )
    b = (
        "ns-client-bavo-task-script-lhc-plate-reader-echo-catmetrics/to/"
        "somewhere/far/far/away/notfoo.bar"
    )
    c = "ns-task-script-hello-world/Lab1"

    path_list = [a, b]
    print(f"This:\n{path_list}")
    paths, filenames = split_paths(path_list)

    processed_paths = process_paths(paths)

    for i, pp in enumerate(filenames):
        processed_paths[i] = path.join(processed_paths[i], pp)

    print(f"Becomes this:\n{processed_paths}")
