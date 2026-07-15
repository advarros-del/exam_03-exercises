def hidenp(small: str, big: str) -> bool:
    it = iter(big)
    return all(c in it for c in small)
    

#def main():
#    print(hidenp("abc", "a1b2c3"))
#    print(hidenp("ace", "abcde"))
#    print(hidenp("aec", "abcde"))
#    print(hidenp("", "abc"))
#    print(hidenp("abc", "ab"))
#    print(hidenp("aaaa", "aaa"))
#    print(hidenp("sing","subsequence testing"))


#if __name__ == "__main__":
#    main()