def greet(name):
    print("hello", name, "!")
    greet2(name)
    print("gretting ready to say bye...")
    bye()


def greet2(name):
    print("how are you, ", name, "?")


def bye():
    print("ok bye!")


if __name__ == "__main__":
    greet("maggie")
