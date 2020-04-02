import re

HEADING_RE = re.compile(r'^(!+)')
def is_heading(line: str):
    return HEADING_RE.match(line)

def convert_heading(heading: str, match: re.match) -> str:
    heading_level = len(match.group(1))
    return re.sub(HEADING_RE, '#' * heading_level, heading)

