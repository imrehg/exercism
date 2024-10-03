from string import ascii_lowercase

alphabet = ascii_lowercase
encode_map = {ord(a): ord(r) for a, r in zip(alphabet, reversed(alphabet))}
decode_map = {ord(r): ord(a) for a, r in zip(alphabet, reversed(alphabet))}


def encode(plain_text: str):
    plain_text = "".join(filter(str.isalnum, plain_text.lower()))
    encoded_text = plain_text.translate(encode_map)
    chunked_text = " ".join([encoded_text[i : i + 5] for i in range(0, len(encoded_text), 5)])
    return chunked_text


def decode(ciphered_text: str) -> str:
    ciphered_text = "".join(filter(str.isalnum, ciphered_text.lower()))
    decoded_text = ciphered_text.translate(decode_map)
    return decoded_text
