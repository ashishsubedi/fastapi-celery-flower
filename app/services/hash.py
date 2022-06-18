from copy import copy

FIX_LEN_STRING: str = "a1b2c3d4e5f6g7"


def my_complex_hash(value: str):
    hash = list(FIX_LEN_STRING)
    value = str(value)
    value2 = value[::-1]

    for i in range(100000000):
        idx = i % len(FIX_LEN_STRING)
        hash[idx] = value2[i % len(value)]

    return "".join(hash)


def main():
    print(my_complex_hash("asdf"))


if __name__ == "__main__":
    main()
