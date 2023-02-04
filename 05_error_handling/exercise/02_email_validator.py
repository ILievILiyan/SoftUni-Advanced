import re


class NameTooShort(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


search_pattern = r'([\w+]+)?(@)?([a-zA-Z]+)?(.)?([a-zA-Z0-9]+)\b'
valid_domain_ends = ["com", "bg", "org", "net"]

while True:
    command = input()
    if command == "End":
        break

    email = command
    result = re.search(search_pattern, email)

    email_name = result.group(1) if result.group(1) else None
    symbol = result.group(2) if result.group(2) else None
    domain_end = result.group(5) if result.group(5) else None

    if len(email_name) < 4:
        raise NameTooShort("Name must be more than 4 characters")
    elif symbol != "@":
        raise MustContainAtSymbolError("Email must contain @")
    elif domain_end not in valid_domain_ends:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        print("Email is valid")
