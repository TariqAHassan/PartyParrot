from party_parrot.parrot_engine import ParrotLang


def to_parrot(string, key=1, copy=False):
    return ParrotLang(encryption_key=key).to_parrot(string, copy=copy)


def from_parrot(string, key=1, copy=False):
    return ParrotLang(encryption_key=key).from_parrot(string, copy=copy)
