from time import sleep


def print_item(list):
    for item in list:
        sleep(1)
        print(item)


if __name__ == "__main__":
    print_item([2, 4, 6, 8, 10])
