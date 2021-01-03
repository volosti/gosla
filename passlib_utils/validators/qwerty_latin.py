from math import log2, log10, log1p, log


LOWER_CASE = (
    '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=',
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\',
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\'',
    'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/')

UPPER_CASE = (
    '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+',
    'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|',
    'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"',
    'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?')

ADJACENCY_MAP = {
    '`': ('`', '1', 'q',
          '~', '!', 'Q'),
    '1': ('1', '2', 'w', 'q', '`',
          '!', '@', 'W', 'Q', '~'),
    '2': ('2', '3', 'e', 'w', 'q', '1',
          '@', '#', 'E', 'W', 'Q', '!'),
    '3': ('3', '4', 'r', 'e', 'w', '2',
          '#', '$', 'R', 'E', 'W', '@'),
    '4': ('4', '5', 't', 'r', 'e', '3',
          '$', '%', 'T', 'R', 'E', '#'),
    '5': ('5', '6', 'y', 't', 'r', '4',
          '%', '^', 'Y', 'T', 'R', '$'),
    '6': ('6', '7', 'u', 'y', 't', '5',
          '^', '&', 'U', 'Y', 'T', '%'),
    '7': ('7', '8', 'i', 'u', 'y', '6',
          '&', '*', 'I', 'U', 'Y', '^'),
    '8': ('8', '9', 'o', 'i', 'u', '7',
          '*', '(', 'O', 'I', 'U', '&'),
    '9': ('9', '0', 'p', 'o', 'i', '8',
          '(', ')', 'P', 'O', 'I', '*'),
    '0': ('0', '-', '[', 'p', 'o', '9',
          ')', '_', '{', 'P', 'O', '('),
    '-': ('-', '=', ']', '[', 'p', '0',
          '_', '+', '}', '{', 'P', ')'),
    '=': ('=', '\\', ']', '[', '-',
          '+', '|', '}', '{', '_'),
    
    'q': ('q', '1', '2', 'w', 'a',
          'Q', '!', '@', 'W', 'A'),
    'w': ('w', '2', '3', 'e', 's', 'a', 'q',
          'W', '@', '#', 'E', 'S', 'A', 'Q'),
    'e': ('e', '3', '4', 'r', 'd', 's', 'w',
          'E', '#', '$', 'R', 'D', 'S', 'W'),
    'r': ('r', '4', '5', 't', 'f', 'd', 'e',
          'R', '$', '%', 'T', 'F', 'D', 'E'),
    't': ('t', '5', '6', 'y', 'g', 'f', 'r',
          'T', '%', '^', 'Y', 'G', 'F', 'R'),
    'y': ('y', '6', '7', 'u', 'h', 'g', 't',
          'Y', '^', '&', 'U', 'H', 'G', 'T'),
    'u': ('u', '7', '8', 'i', 'j', 'h', 'y',
          'U', '&', '*', 'I', 'J', 'H', 'Y'),
    'i': ('i', '8', '9', 'o', 'k', 'j', 'u',
          'I', '*', '(', 'O', 'K', 'J', 'U'),
    'o': ('o', '9', '0', 'p', 'l', 'k', 'i',
          'O', '(', ')', 'P', 'L', 'K', 'I'),
    'p': ('p', '0', '-', '[', ';', 'l', 'o',
          'P', ')', '_', '{', ':', 'L', 'O'),
    '[': ('[', '-', '=', ']', "'", ';', 'p',
          '{', '_', '+', '}', '"', ':', 'P'),
    ']': (']', '=',     '\\', "'", '[',
          '}', '+',      '|', '"', '{'),
    '\\': ('\\',                   ']',
           '|',                    '}'),
    'a': ('a', 'q', 'w', 's', 'z',           'b',
          'A', 'Q', 'W', 'S', 'Z',           'B'),
    's': ('s', 'w', 'e', 'd', 'x', 'z', 'a',
          'S', 'W', 'E', 'D', 'X', 'Z', 'A'),
    'd': ('d', 'e', 'r', 'f', 'c', 'x', 's',
          'D', 'E', 'R', 'F', 'C', 'X', 'S'),
    'f': ('f', 'r', 't', 'g', 'v', 'c', 'd', 'e',
          'F', 'R', 'T', 'G', 'V', 'C', 'D', 'E'),
    'g': ('g', 't', 'y', 'h', 'b', 'v', 'f',
          'G', 'T', 'Y', 'H', 'B', 'V', 'F'),
    'h': ('h', 'y', 'u', 'j', 'n', 'b', 'g',
          'H', 'Y', 'U', 'J', 'N', 'B', 'G'),
    'j': ('j', 'u', 'i', 'k', 'm', 'n', 'h',
          'J', 'U', 'I', 'K', 'M', 'N', 'H'),
    'k': ('k', 'i', 'o', 'l', ',', 'm', 'j',
          'K', 'I', 'O', 'L', '<', 'M', 'J'),
    'l': ('l', 'o', 'p', ';', '.', ',', 'k',
          'L', 'O', 'P', ':', '>', '<', 'K'),
    ';': (';', 'p', '[', "'", '.', 'l',
          ':', 'P', '{', '"', '>', 'L'),
    "'": ("'", '[', ']', '/',
          '"', '{', '}', '?'),

    'z': ('z', 'a', 's', 'x',
          'Z', 'A', 'S', 'X'),
    'x': ('x', 's', 'd', 'c', 'z',
          'X', 'S', 'D', 'C', 'Z'),
    'c': ('c', 'd', 'f', 'v', 'x',           'b',
          'C', 'D', 'F', 'V', 'X',           'B'),
    'v': ('v', 'f', 'g', 'b', 'c',
          'V', 'F', 'G', 'B', 'C'),
    'b': ('b', 'g', 'h', 'n', 'v',           'a', 'c',
          'B', 'G', 'H', 'N', 'V',           'A', 'C'),
    'n': ('n', 'h', 'j', 'm', 'b',
          'N', 'H', 'J', 'M', 'B'),
    'm': ('m', 'j', 'k', ',', 'n',
          'M', 'J', 'K', '<', 'N'),
    ',': (',', 'k', 'l', '.', 'm',
          '<', 'K', 'L', '>', 'M'),
    '.': ('.', 'l', ';', '/', ',',
          '>', 'L', ':', '?', '<'),
    '/': ('/', ';', "'",     '.',
          '?', ':', '"',     '>'),

    ' ': (' ', 'x', 'c', 'v', 'b', 'n', 'm', ',',
               'X', 'C', 'V', 'B', 'N', 'M', '<'),
}

for lc, uc in zip(LOWER_CASE, UPPER_CASE):
    ADJACENCY_MAP[uc] = ADJACENCY_MAP[lc]


class QwertyValidator:
    adjacency_map = ADJACENCY_MAP
    lower_case = LOWER_CASE
    upper_case = UPPER_CASE

    adjacency_level_1 = 0.0625
    adjacency_level_2 = 0.25
    adjacency_level_3 = 1
    adjacency_level_4 = 2

    lower_case_to_lower = 0.875
    upper_case_to_upper = 1
    upper_case_to_lower = 1.125
    lower_case_to_upper = 1.25

    def compare_adjacency(self, previous, next_):
        if next_ in self.adjacency_map[previous]:
            return self.adjacency_level_1
        for i in self.adjacency_map[previous]:
            if next_ in self.adjacency_map[i]:
                return self.adjacency_level_2
        for i in self.adjacency_map[previous]:
            for j in self.adjacency_map[i]:
                if next_ in self.adjacency_map[j]:
                    return self.adjacency_level_3
        return self.adjacency_level_4

    def compare_cases(self, previous, next_):
        if previous in self.lower_case:
            if next_ in self.upper_case:
                return self.lower_case_to_upper
            elif next_ in self.lower_case:
                return self.lower_case_to_lower
        elif previous in self.upper_case:
            if next_ in self.lower_case:
                return self.upper_case_to_lower
            elif next_ in self.upper_case:
                return self.upper_case_to_upper
        raise ValueError

    def compare_families(self, previous: str, next_: str):
        if previous.isalpha():
            if next_.isalpha():
                return 0.875
            return 1.125
        elif previous.isdecimal():
            if next_.isdecimal():
                return 0.75
            return 1
        else:
            if next_.isalpha():
                return 1.25
            if next_.isdecimal():
                return 1.25
            return 0.875

    def validate(self, secret: str):
        complexity_count = 0
        for previous, next_ in zip(secret[0:-1], secret[1:]):
            complexity_count += (
                self.compare_adjacency(previous, next_)
                * self.compare_cases(previous, next_)
                * self.compare_families(previous, next_)
                * len(set(secret)) / len(secret)
            )
        return complexity_count
