def response(hey_bob: str) -> str:
    hey_bob = hey_bob.strip()

    if hey_bob == "":
        return "Fine. Be that way!"

    is_yelling = hey_bob.isupper()
    is_question = hey_bob[-1] == "?"

    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    if is_yelling:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."

    return "Whatever."
