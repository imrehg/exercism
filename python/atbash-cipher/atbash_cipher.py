from string import ascii_lowercase

encode_map = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])


def encode(plain_text: str, chunked: bool = True):
    plain_text = "".join(filter(str.isalnum, plain_text.lower()))
    encoded_text = plain_text.translate(encode_map)
    if chunked:
        encoded_text = " ".join([encoded_text[i : i + 5] for i in range(0, len(encoded_text), 5)])
    return encoded_text


def decode(ciphered_text: str) -> str:
    return encode(ciphered_text, chunked=False)
