def whisper_cipher(text: str, shift: int) -> str:
    result = ""
    for c in text:
        if c.islower():
            key = ord(c)
            key = key - ord("a")
            key = key + shift
            key = key % 26
            key = key + ord("a")
            result += chr(key)
        elif c.isupper():
            key = ord(c)
            key = key - ord("A")
            key = key + shift
            key = key % 26
            key = key + ord("A")
            result += chr(key)
        else:
            result += c
            
    return text