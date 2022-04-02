def convert(number: int) -> str:
    result = ""

    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"

    if result == "":  # None of the above are factors
        result = str(number)

    return result
