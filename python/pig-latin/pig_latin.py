import re

# Matching patterns for the various Pig Latin grammar rules and their transformations
rule_1 = re.compile(r"^([aeiou]|yt|xr)\w*$")
rule_1_sub = r"\g<0>ay"

rule_2_3 = re.compile(r"^(?P<start>[^aeiou]?qu|[^aeiou]+)(?P<rest>\w*)$")
rule_4 = re.compile(r"^(?P<start>[^aeiou]+)(?P<rest>y\w*)$")
rule_2_3_4_sub = r"\g<rest>\g<start>ay"


def translate(text: str) -> str:
    """Translate a text to Pig Latin. Tnslatetray aay exttay otay Igpay Atinlay."""

    words = re.split(r"\s+", text)
    for i, word in enumerate(words):
        for rule, transform in (
            (rule_1, rule_1_sub),
            (rule_4, rule_2_3_4_sub),
            (rule_2_3, rule_2_3_4_sub),
        ):
            word, subs_done = rule.subn(transform, word)
            if subs_done:
                break
        words[i] = word

    return " ".join(words)
