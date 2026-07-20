def twist_sequence(arr: list[int], k: int) -> list[int]:
    for i in range(k):
        jajaj = arr.pop()
        arr.insert(0, jajaj)
    return arr