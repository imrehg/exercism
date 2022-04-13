import re

HEADER_PATTERN = re.compile("(?P<header>#{1,6}) (?P<title>.*)")
LIST_PATTERN = re.compile(r"\* (?P<content>.*)")
BOLD_PATTERN = re.compile("(?P<before>.*)__(?P<content>.*?)__(?P<after>.*)")
ITALIC_PATTEN = re.compile("(?P<before>.*)_(?P<content>.*?)_(?P<after>.*)")


def enclose_in_tag(tag: str, content: str) -> str:
    return f"<{tag}>{content}</{tag}>"


def find_pattern_and_convert_all(
    pattern: re.Pattern, tag: str, line: str
) -> str:
    while m := pattern.search(line):
        line = (
            m.group("before")
            + enclose_in_tag(tag, m.group("content"))
            + m.group("after")
        )
    return line


def convert_bold(line: str) -> str:
    return find_pattern_and_convert_all(BOLD_PATTERN, "strong", line)


def convert_italic(line: str) -> str:
    return find_pattern_and_convert_all(ITALIC_PATTEN, "em", line)


def parse(markdown: str) -> str:
    """Parse a markdown string according to formatting rules into HTML."""
    html = ""
    in_list = False
    lines = markdown.split("\n")
    for line in lines:
        transformed = False
        if m := HEADER_PATTERN.match(line):
            transformed = True
            h_number = len(m.group("header"))
            line = enclose_in_tag(f"h{h_number}", m.group("title"))
        elif m := LIST_PATTERN.match(line):
            transformed = True
            line = enclose_in_tag("li", m.group("content"))
            if not in_list:
                in_list = True
                line = "<ul>" + line
        elif in_list:
            in_list = False
            html += "</ul>"

        if not transformed:
            line = "<p>" + line + "</p>"
        line = convert_bold(line)
        line = convert_italic(line)
        html += line
    if in_list:
        html += "</ul>"
    return html
