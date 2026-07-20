def string_sculptor(text: str) -> str:
    text = text.lower()
    flag = False
    result = ""
    for c in text:
        if c.isspace():
            flag = False
            result +=  c
        if c.isalpha() and flag == True:
            result +=  c.upper()
            flag = not flag
        if c.isalpha() and flag == False:
            result +=  c
            flag = not flag
    return result