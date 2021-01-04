from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Dict, Set


def gen_alphabet_map(tuple_):
    dict_ = {}
    for i in range(len(tuple_)):
        previous = tuple_[i - 1]
        next_ = tuple_[i + 1] if i < len(tuple_) - 1 else tuple_[0]
        dict_[tuple_[i]] = {previous, next_, previous.upper(), next_.upper()}
        dict_[tuple_[i].upper()] = dict_[tuple_[i]]
    return dict_


def merge_maps(a: 'Dict[str, Set]', b: 'Dict[str, Set]'):
    return {k: {*a.get(k, set()), *b.get(k, set())} for k in {*a.keys(), *b.keys()}}
