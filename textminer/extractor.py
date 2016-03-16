import re


def phone_numbers(arg):
    match = re.findall(r"(\([0-9]{3}\) ?[0-9]{3}-?[0-9]{4})", arg)
    if match:
        return match


def emails(arg):
    matches = re.findall(r"(([a-z]*|[a-z\.]*)@([a-z]*)\.([a-z]{2,3}))", arg)
    if matches:
        return [match[0] for match in matches]