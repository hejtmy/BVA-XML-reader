from collections import defaultdict


def flatten_list(list_of_lists):
    return([item for sublist in list_of_lists for item in sublist])


def find_duplicates(mylist):
    # https://stackoverflow.com/questions/11236006/identify-duplicate-values-in-a-list-in-python
    D = defaultdict(list)
    for i, item in enumerate(mylist):
        D[item].append(i)
    D = {k: v for k, v in D.items() if len(v) > 1}
    # returns hash like {20: [0, 3], 30: [1, 4]}
    i_duplicates = []
    for k in D.keys():
        i_duplicates += D[k][1:]
    return i_duplicates


def remove_at_indices(mylist, indices):
    return [i for j, i in enumerate(mylist) if j not in indices]
