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


def completion_layout_map(ALPHABET_MAP, lower_case_map):
    for key, set_ in ALPHABET_MAP.items():
        values = set_.copy()
        for value in values:
            ALPHABET_MAP[key].add(lower_case_map[value])
    keys = tuple(ALPHABET_MAP.keys())
    for key in keys:
        ALPHABET_MAP[lower_case_map[key]] = ALPHABET_MAP[key]
    return ALPHABET_MAP
