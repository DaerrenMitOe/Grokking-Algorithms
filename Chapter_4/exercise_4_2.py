def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])


if __name__ == "__main__":
    print(count([1, 2, 3, 4]))
