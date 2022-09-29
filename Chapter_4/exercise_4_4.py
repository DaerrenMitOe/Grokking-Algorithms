def binary_search(list, item):
    if len(list) == 1:
        return list[0]
    else:
        mid = len(list) // 2
        if list[mid] > item:
            return binary_search(list[:mid], item)
        else:
            return binary_search(list[mid:], item)


if __name__ == "__main__":
    print(binary_search([1, 2, 3, 4], 4))
