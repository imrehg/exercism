from string import ascii_lowercase

encode_map = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])
decode_map = str.maketrans(ascii_lowercase[::-1], ascii_lowercase)


def encode(plain_text: str):
    plain_text = "".join(filter(str.isalnum, plain_text.lower()))
    encoded_text = plain_text.translate(encode_map)
    chunked_text = " ".join([encoded_text[i : i + 5] for i in range(0, len(encoded_text), 5)])
    return chunked_text


def decode(ciphered_text: str) -> str:
    ciphered_text = "".join(filter(str.isalnum, ciphered_text.lower()))
    decoded_text = ciphered_text.translate(decode_map)
    return decoded_text
