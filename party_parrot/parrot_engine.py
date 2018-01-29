"""

    Engine
    ~~~~~~

"""
from sklearn.utils import shuffle
from string import ascii_lowercase as letters
from party_parrot._utils import parrot_splitter


class ParrotLang(object):
    def __init__(self, encryption_key=1):
        # Shuffle
        from party_parrot._slack_parrots import parrots
        parrots = shuffle(parrots, random_state=encryption_key)

        # Look up dicts
        self._letter_par = {letter: par for letter, par in zip(letters, parrots)}
        self._par_letter = {v: k for k, v in self._letter_par.items()}

    def _get(self, key, direction):
        d = self._letter_par if direction == 'forward' else self._par_letter
        return d[key] if key in d else key

    def _mapper(self, string, direction):
        string = string.lower()
        to_map = string if direction == 'forward' else parrot_splitter(string)
        mapped = map(lambda key: self._get(key, direction=direction), to_map)
        return "".join(mapped)

    def to_parrot(self, string):
        return self._mapper(string, direction="forward")

    def from_parrot(self, string):
        return self._mapper(string, direction="reverse")
