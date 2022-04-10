import re


def enclose_in_tag(tag, content):
    return f"<{tag}>{content}</{tag}>"

HEADER = re.compile("(?P<header>#{1,6}) (?P<title>.*)")
BOLD = re.compile("(?P<before>.*)__(?P<content>.*)__(?P<after>.*)")
ITALIC = re.compile("(?P<before>.*)_(?P<content>.*)_(?P<after>.*)")

def convert_italic(line:str)->str:
    if m := re.match("(?P<before>.*)_(?P<content>.*)_(?P<after>.*)", line):
        return m.group("before") + enclose_in_tag("em", m.group("content")) + m.group("after")       
    return line 

def parse(markdown):
    lines = markdown.split("\n")
    res = ""
    in_list = False
    in_list_append = False
    for i in lines:
        if m := HEADER.match(i):
            h_number = len(m.group("header"))
            i = enclose_in_tag(f"h{h_number}", m.group("title"))
        m = re.match(r"\* (.*)", i)
        if m:
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match("(.*)__(.*)__(.*)", curr)
                if m1:
                    curr = (
                        m1.group(1)
                        + enclose_in_tag("strong", m1.group(2))
                        + m1.group(3)
                    )
                    is_bold = True
                m1 = re.match("(.*)_(.*)_(.*)", curr)
                if m1:
                    # This might not be tested properly
                    curr = (
                        m1.group(1)
                        + enclose_in_tag("em", m1.group(2))
                        + m1.group(3)
                    )
                    is_italic = True
                i = "<ul>" + enclose_in_tag("li", curr)
            else:
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match("(.*)__(.*)__(.*)", curr)
                if m1:
                    is_bold = True
                m1 = re.match("(.*)_(.*)_(.*)", curr)
                if m1:
                    is_italic = True
                if is_bold:
                    curr = (
                        m1.group(1)
                        + "<strong>"
                        + m1.group(2)
                        + "</strong>"
                        + m1.group(3)
                    )
                if is_italic:
                    curr = (
                        m1.group(1)
                        + "<em>"
                        + m1.group(2)
                        + "</em>"
                        + m1.group(3)
                    )
                i = "<li>" + curr + "</li>"
        else:
            if in_list:
                in_list_append = True
                in_list = False

        m = re.match("<h|<ul|<p|<li", i)
        if not m:
            i = "<p>" + i + "</p>"
        m = re.match("(.*)__(.*)__(.*)", i)
        if m:
            i = m.group(1) + "<strong>" + m.group(2) + "</strong>" + m.group(3)
        i = convert_italic(i)
        if in_list_append:
            i = "</ul>" + i
            in_list_append = False
        res += i
    if in_list:
        res += "</ul>"
    return res
