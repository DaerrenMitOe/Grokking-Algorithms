def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])


if __name__ == "__main__":
    print(sum([1, 2, 3, 4]))
