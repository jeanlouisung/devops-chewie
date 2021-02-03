def add(nb1: int, nb2: int):
    if type(nb1) != int or type(nb2) != int:
        raise TypeError(f"Arguments should be int")
    res = nb1 + nb2
    return res


if __name__ == '__main__':
    print(add(0, 0))
