import re


def binary(arg):
    match = re.search(r"[01]*", arg)
    if match:
        return match.group()


def binary_even(arg):
    even_match = re.search(r"(0*)?$", arg)
    if even_match:
        return even_match.group()


def hex(arg):
    hexadex = re.search(r"[0-9a-fA-F]+[^OFE]", arg)
    if hexadex:
        return hexadex.group()


def word(arg):
    wordy = re.search(r"\D\w-?[^*]\w", arg)
    if wordy:
        return wordy.group()


def words(arg, count=0):
    counter = re.findall(r".\w+-?\s?[\w]+\s?[\w]+[^!]", arg)
    if count:
        for item in counter:
            if len(item.split()) == count:
                return counter
    elif counter:
        return counter


def phone_number(arg):
    match = re.search(r"\(?(\d{3})\)?[\.\-\s]?(\d{3})[\.\-]?(\d{4})", arg)
    if match:
        return match.group()


def money(arg):
    match = re.search(r"^\$(\d+|\d{1,3}(,\d{3})*)(\.[0-9]{2})?$", arg)
    if match:
        return match.group()

def zipcode(arg):
    match = re.search(r"^([0-9]{5})-?([0-9]{4})?$", arg)
    if match:
        return match.group()

def date(arg):
    match = re.search(r"(((\d{4})(-?|\/?)(\d{1,2})(-?|\/?)(\d{2}))|((\d{1,2})(-?|\/?)(\d{1,2})(-?|\/?)(\d{4})))", arg)
    if match:
        return match.group()