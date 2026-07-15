def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    result = matrix
    for i, the_list in enumerate(result):
        result[i] = the_list[::-1]
    return result

#def main():
#    print(mirror_matrix([[1,2,3],[4,5,6]]))
#    print(mirror_matrix([[1,2],[3,4],[5,6]]))
#    print(mirror_matrix([[7]]))
#    print(mirror_matrix([[1,2,3,4]]))

#if __name__ == "__main__":
#    main()