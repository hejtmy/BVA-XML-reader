from collections import defaultdict
from datetime import datetime


# ' Heavily needs description
def element_to_row(element):
    keys = flatten_list([[element.tag + "_" + x] for x in list(element.attrib.keys())])
    values = list(element.attrib.values())
    for el in element:
        tag = el.tag
        tag_keys = list(el.attrib.keys())
        keys += flatten_list([[tag + "_" + x] for x in tag_keys])
        tag_values = list(el.attrib.values())
        values += tag_values
        value = el.text
        if value is not None:
            keys += [tag + "_value"]
            values += [str(value)]
        children_keys, child_values = element_to_row(el)
        keys, values = keys + children_keys, values + child_values
    i_duplicate = find_duplicates(keys)
    keys, values = remove_at_indices(keys, i_duplicate), remove_at_indices(values, i_duplicate)
    return keys, values


# ' Converts XML BVA timestamp to POSIX timestamp
def real_timestamp(element):
    # timestamp real is in form of 01/29/2019 10:02:45.574
    dt = datetime.strptime(element.find('TimestampReal').text,
                           '%m/%d/%Y %H:%M:%S.%f')
    return(float(dt.timestamp()))


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
