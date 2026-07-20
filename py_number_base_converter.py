def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    if number.isalnum():
        return "ERROR"
    if not (2 <= from_base <= 36) or not (2 <= to_base <= 36):
        return "ERROR"
    the_base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in number:
        if c not in the_base[:from_base]:
            return "ERROR"
    decimal = 0
    for c in number:
        num_val = the_base.index(c)
        decimal = decimal * from_base + num_val
    result = ""
    while decimal > 0:
        rest = decimal % to_base
        result = the_base[rest] + result
        decimal = decimal // from_base
    return result

    