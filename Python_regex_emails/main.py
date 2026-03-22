import re

with open("emails.txt") as file:
    emails = file.read()


    pattern = r"[a-zA-Z0-9-_\.]+@"
    pattern = r"[a-zA-Z0-9-_\.]+@[a-zA-Z-]+"
    pattern = r"[a-zA-Z0-9-_\.]+@[a-zA-Z-]+\.com"


    matches_result = re.finditer(pattern, emails)

    for match in matches_result:
        print(match.group())

