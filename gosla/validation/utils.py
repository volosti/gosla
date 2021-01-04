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
    for key, values in base_qwerty_map.items():
        values_ = values.copy()
        for value in values_:
            base_qwerty_map[key].add(lower_case_map[value])
    keys = tuple(base_qwerty_map.keys())
    for key in keys:
        base_qwerty_map[lower_case_map[key]] = base_qwerty_map[key]
    return base_qwerty_map