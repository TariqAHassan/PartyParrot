from party_parrot.parrot_engine import ParrotLang


def to_parrot(string, encryption_key=1):
    return ParrotLang(key=encryption_key).to_parrot(string)


def from_parrot(string, encryption_key=1):
    return ParrotLang(key=encryption_key).from_parrot(string)
