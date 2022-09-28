def function_name():
    a = str(2)
    try:
        b = 3 + a
    except TypeError:
        print("a is not an integer")


def main():
    function_name()


if __name__ == "__main__":
    main()
