def countdown(i):
    print(i)

    if i <= 1:
        return
    else:
        countdown(i - 1)


if __name__ == "__main__":
    countdown(3)
