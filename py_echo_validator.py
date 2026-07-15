def echo_validator(text: str) -> bool:
    if len(text) == 0:
        return False
    new_text = text.lower()
    new_text = new_text.replace(" ", "")
    if new_text == new_text[::-1]:
        return True
    else:
    	return False

#def main() -> None:
#    print(echo_validator("racecar"))
#    print(echo_validator("A man a plan a canal Panama"))
#    print(echo_validator("race a car"))
#    print(echo_validator("Was it a car or a cat I saw"))
#    print(echo_validator("hello"))
#    print(echo_validator("Madam Im Adam"))
#    print(echo_validator(""))
    
#if __name__ == "__main__":
#    main()