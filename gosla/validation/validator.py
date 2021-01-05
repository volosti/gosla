from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Dict, Set


class ComplexityValidator:
    adjacency_map: 'Dict[str, Set[str]]'

    adjacency_level_1 = 0.0625
    adjacency_level_2 = 0.25
    adjacency_level_3 = 1
    adjacency_level_4 = 2

    lower_case_to_lower = 0.875
    upper_case_to_upper = 1
    upper_case_to_lower = 1.125
    lower_case_to_upper = 1.25

    password_max_len = 4096

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
        if len(secret) >= self.password_max_len:
            raise ValueError
        complexity_count = 0
        for previous, next_ in zip(secret[0:-1], secret[1:]):
            complexity_count += (
                self.compare_adjacency(previous, next_)
                * self.compare_cases(previous, next_)
                * self.compare_families(previous, next_)
                * len(set(secret)) / len(secret)
            )
        return complexity_count
