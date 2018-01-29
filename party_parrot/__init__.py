from party_parrot.parrot_engine import ParrotLang


def to_parrot(string, key=1):
    return ParrotLang(encryption_key=key).to_parrot(string)


def from_parrot(string, key=1):
    return ParrotLang(encryption_key=key).from_parrot(string)
