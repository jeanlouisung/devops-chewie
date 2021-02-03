
def add(nb1: int, nb2: int):
    if type(nb1) is not 'int' or type(nb2) is not 'int':
        raise TypeError(f"Arguments should be int")
    return 0


if __name__ == '__main__':
    print(add(0, 0))
