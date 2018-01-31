"""

    Utils
    ~~~~~

"""
import re


def get_parrots(string):
    return re.findall(r'(:.*?:)', string)


def dict_str_replace(string, d, swap_key_value=False):
    for k, v in d.items():
        if swap_key_value:
            k, v = v, k
        string = string.replace(k, v)
    return string
