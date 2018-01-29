from party_parrot.parrot_engine import ParrotLang

_pl = ParrotLang()


def to_parrot(string):
    return _pl.to_parrot(string)


def from_parrot(string):
    return _pl.from_parrot(string)
