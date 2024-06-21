from os import path
from typing import Iterable, Tuple


def split_files(paths: Iterable[str]) -> Tuple[Tuple[str], Tuple[str]]:
    split_blocks = [path.split(p) for p in paths]

    paths, files = zip(*((p, f) for p, f in split_blocks))

    return paths, files


def create_final_list(paths):
    return len(paths) * [""]


def create_box_list(paths):
    splits = [i.split("/") for i in paths]
    print(splits)
    max_path_len = max(map(len, splits))
    #  box_list = max_path_len

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
    c = "ns-task-script-hello-world/Lab1"

    path_list = [a, b, c]
    paths, filenames = split_files(path_list)

    final_list = create_final_list(paths)

    create_box_list(path_list)
