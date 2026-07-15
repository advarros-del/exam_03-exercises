def vocals_counter(string):
	vocals = "aeiou"
	return sum(1 for c in string.lower() if c in vocals)

def tuplating(string):
    return(len(string), string.lower(), vocals_counter(string))

def cryptic_sorter(strings: list[str]) -> list[str]:
    lenght: int = len(strings)
    result = strings
    
    for i in range(1, lenght):
        the_string = result[i]
        the_tuplex = tuplating(the_string)
        j = i - 1
        while j >= 0 and tuplating(result[j]) > the_tuplex:
            result[j + 1] = result[j]
            j -= 1
            print("dentro de bucle")
            print(result)
        result[j + 1] = the_string
        print("fuera de bucle")
        print(result)
    return result

def main() -> None:
    #print(cryptic_sorter(["hola"]))
    print(cryptic_sorter(["apple","cat","banana","dog","elephant"]))
    #print(cryptic_sorter(["aaa","bbb","AAA","BBB"]))
    #print(cryptic_sorter(["hello","world","hi","test"]))
    #print(cryptic_sorter([]))
    #print(cryptic_sorter([""]))


if __name__ == "__main__":
    main()

