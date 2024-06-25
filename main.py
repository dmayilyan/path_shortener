from itertools import zip_longest
from collections import deque
from os import path
from typing import Iterable, Tuple, List


def split_paths(paths: Iterable[str]) -> Tuple[List[str], Tuple[str]]:
    split_blocks = [path.split(p) for p in paths]

    paths, files = zip(*((p, f) for p, f in split_blocks))
    paths = [i.split("/") for i in paths]

    return paths, files


def create_final_list(paths) -> List[str]:
    return [[] for _ in paths]


def process_paths(paths, final_list):
    for i, slice_list in enumerate(zip_longest(*paths, fillvalue="")):
        if all(map(lambda x: x < 10, map(len, slice_list))):
            for pathi, p in enumerate(slice_list):
                final_list[pathi].append(p)
            continue

        max_in_slice = max(map(len, slice_list))
        slice_list = [i.ljust(max_in_slice, chr(0)) for i in slice_list]
        #  print(slice_list)

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

        buffer_list = create_final_list(slice_list)
        for vals in zip(*slice_list, final_mask):
            if len(set(vals[:-1])) == 1 and not vals[-1]:
                for vali in range(len(vals[:-1])):
                    if not buffer_list[vali-1] == ".":
                        buffer_list[vali].append(".")
            else:
                for vali in range(len(vals[:-1])):
                    buffer_list[vali].append(vals[vali].strip(chr(0)))


        buffer_list = ["".join(item) for item in buffer_list]

        for bi, fi in zip(buffer_list, final_list):
            fi.append(bi)

        print("!!!", final_list)



    print(final_list)
    print("/".join(final_list[0]))




#  splits = a.split("/"), b.split("/")


#  final_slices = []
#  for i in range(len(slice_list)):
    #  final_slices.append("")


#  for i_slice in range(max(map(len, splits))):
    #  dots = False
    #  slice_list = []
    #  for s in splits:
        #  try:
            #  slice_list.append(s[i_slice])
        #  except IndexError as e:
            #  continue

    #  max_in_slice = max(map(len, slice_list))

    #  if max_in_slice < 10:
        #  for sli, sl in enumerate(slice_list):
            #  final_slices[sli] += "/" + sl
        #  continue

    #  slice_list = [i.ljust(max_in_slice, chr(0)) for i in slice_list]
    #  # print(slice_list)

    #  mask = []
    #  for vals in zip(*slice_list):
        #  if len(set(vals)) != 1:
            #  mask.append(True)
        #  else:
            #  mask.append(False)

    #  surround_size = 2

    #  mask_shifted = mask.copy()
    #  mask_shifted += [False] * surround_size
    #  mask_shifted = mask_shifted[surround_size:]
    #  final_mask = [a or b for a, b in zip(mask, mask_shifted)]

    #  for vals in zip(*slice_list, final_mask):
        #  if len(seatht(vals[:-1])) == 1 and not vals[-1]:
            #  for i in range(len(vals[:-1])):
                #  if not final_slices[i].startswith("..."):
                    #  final_slices[i] += "..."
        #  else:
            #  for i in range(len(vals[:-1])):
                #  final_slices[i] += vals[i].strip(chr(0))


#  print(final_slices)


if __name__ == "__main__":
    a = "ns-client-bavo-protocol-manual-lhc-mellinbright-catmetrics/to/somewhere/far/far/away/foo.bar"
    b = "ns-client-bavo-task-script-lhc-plate-reader-echo-catmetrics/to/somewhere/far/far/away/notfoo.bar"
    #  c = "ns-task-script-hello-world/Lab1"

    path_list = [a, b]
    paths, filenames = split_paths(path_list)

    # TODO
    d = deque()

    final_list = create_final_list(paths)
    print(final_list)

    process_paths(paths, final_list)
