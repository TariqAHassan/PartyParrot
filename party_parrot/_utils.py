"""

    Utils
    ~~~~~

"""
import re


def get_parrots(string):
    return re.findall(r'(:.*?:)', string)


def parrot_splitter(string):
    return re.split('(:.*?:)', string)
