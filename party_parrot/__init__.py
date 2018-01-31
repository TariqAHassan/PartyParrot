from party_parrot.parrot_engine import ParrotLang

_pl = ParrotLang()


def to_parrot(string, key=1, copy=False):
    return _pl.to_parrot(string, key=key, copy=copy)


def from_parrot(string, key=1, copy=False):
    return _pl.from_parrot(string, key=key, copy=copy)
