def pattern_tracker(text: str) -> int:
    counter: int = 0
    for i in range(len(text) -1):
        n:int = 0
        n1: int = 0
        if text[i].isnumeric() and text[i+1].isnumeric():
            n = int(text[i])
            n1 = int(text[i+1])
            if n1 == n + 1: 
                counter += 1
    return counter

def main() -> None:
    print(pattern_tracker("1a23"))


if __name__ == "__main__":
    main()