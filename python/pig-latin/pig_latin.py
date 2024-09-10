import re

# Matching patterns for the various Pig Latin grammar rules
rule_1 = re.compile(r"^([aeiou]|yt|xr)\w*$")
rule_2_3 = re.compile(r"^(?P<start>[^aeiou]?qu|[^aeiou]+)(?P<rest>\w*)$")
rule_4 = re.compile(r"^(?P<start>[^aeiou]+)(?P<rest>y\w*)$")


def translate(text: str) -> str:
    """Translate a text to Pig Latin. Tnslatetray aay exttay otay Igpay Atinlay."""

    words = re.split(r"\s+", text)
    for i, word in enumerate(words):
        # Apply the various
        word, sub_count = rule_1.subn(r"\g<0>ay", word)
        if not sub_count:
            word, sub_count = rule_4.subn(r"\g<rest>\g<start>ay", word)
        if not sub_count:
            word, sub_count = rule_2_3.subn(r"\g<rest>\g<start>ay", word)
        words[i] = word

    return " ".join(words)
