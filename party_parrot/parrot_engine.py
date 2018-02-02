"""

    Engine
    ~~~~~~

"""
import pyperclip
from sklearn.utils import shuffle
from string import ascii_lowercase as chars
from party_parrot._slack_parrots import parrots
from party_parrot._utils import dict_str_replace


class ParrotLang(object):
    def __init__(self):
        self._dicts = dict()
        self._default_key = 1
        self._get_dict(encryption_key=self._default_key)

    def _get_dict(self, encryption_key):
        if encryption_key not in self._dicts:
            self._dicts = dict()  # reset to constrain memory load.
            parrots_shuf = shuffle(parrots, random_state=encryption_key)
            parrot_dict = {char: par for char, par in zip(chars, parrots_shuf)}
            self._dicts[encryption_key] = parrot_dict
        return self._dicts[encryption_key]

    def _mapper(self, string, direction, key, copy):
        if not isinstance(key, int):
            raise TypeError("`key` must be an integer.")

        if key is None:
            key = self._default_key

        string = string.lower()
        d = self._get_dict(encryption_key=key)
        if direction == "forward":
            out = "".join(map(lambda key: d.get(key, key), string))
        else:
            out = dict_str_replace(string, d=d, swap_key_value=True)

        if copy:
            pyperclip.copy(out)
        return out

    def to_parrot(self, string, key=None, copy=False):
        return self._mapper(string, direction="forward", key=key, copy=copy)

    def from_parrot(self, string, key=None, copy=False):
        return self._mapper(string, direction="reverse", key=key, copy=copy)
