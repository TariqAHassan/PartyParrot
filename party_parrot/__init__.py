__version_info__ = (0, 2, 1)
__version__ = '.'.join(map(str, __version_info__))

from party_parrot.parrot_engine import ParrotLang

_pl = ParrotLang()


def to_parrot(string, key=None, copy=False):
    """

    Convert to parrot.

    Args:
        string (str): any string
        key (int): a key to encrypt parrot messages. If None, 1 will be used.
        copy (bool): if True, copy to clipboard.

    Returns
        str: the converted message.

    """
    return _pl.to_parrot(string, key=key, copy=copy)


def from_parrot(string, key=None, copy=False):
    """

    Convert from parrot.

    Args:
        string (str): any string
        key (int): a key to encrypt parrot messages. If None, 1 will be used.
        copy (bool): if True, copy to clipboard.

    Returns
        str: the converted message.

    """
    return _pl.from_parrot(string, key=key, copy=copy)
