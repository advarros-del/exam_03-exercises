def bracket_validator(s: str) -> bool:
    opener: list = ["(", "[", "{"]
    lister:list = []
    pair: dict = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in opener:
            lister.append(c)
        elif c in pair:
            if not lister or lister[-1] != pair[c]:
                return False
            lister.pop()
    if len(lister) != 0:
        return False  
    return True

#def main() -> None:
#    print(bracket_validator("()"))
#    print(bracket_validator("()[]{}"))
#    print(bracket_validator("(]"))
#    print(bracket_validator("([)]"))
#    print(bracket_validator("{[]}"))
#    print(bracket_validator("hello(world)"))
#    print(bracket_validator("((())"))
#    print(bracket_validator(""))


#if __name__ == "__main__":
#    main()
