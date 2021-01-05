from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Dict, Set, Union


def gen_alphabet_map(tuple_):
    dict_ = {}
    for i in range(len(tuple_)):
        previous = tuple_[i - 1]
        next_ = tuple_[i + 1] if i < len(tuple_) - 1 else tuple_[0]
        dict_[tuple_[i]] = {previous, next_, previous.upper(), next_.upper()}
        dict_[tuple_[i].upper()] = dict_[tuple_[i]]
    return dict_


def completion_layout_map(base_qwerty_map, lower_case_map):
    [base_qwerty_map[key].add(key) for key in base_qwerty_map]
    for key, values in base_qwerty_map.items():
        values_ = values.copy()
        for value in values_:
            base_qwerty_map[key].add(lower_case_map[value])
    keys = tuple(base_qwerty_map.keys())
    for key in keys:
        base_qwerty_map[lower_case_map[key]] = base_qwerty_map[key]
    return base_qwerty_map


def merge_layouts_by_keys(first, second):
    merged_layout = first.copy()
    for key, values in second.items():
        merged_layout[key] = {*merged_layout.get(key, set()), *second[key]}
    return merged_layout


def merge_layouts_by_proxy(origin, proxy):
    merged_layout = origin.copy()
    for k, v in proxy.items():
        merged_layout[k] |= merged_layout[v]
        merged_layout[v] |= merged_layout[k]
    return merged_layout
