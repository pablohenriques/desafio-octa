
def search(v: list[int], x: int) -> int:
    for index in range(len(v)):
        if v[index] == x:
            return index
    return -1


def insert(v: list[int], x: int, k: int) -> list[int]:
    if len(v) < 1:
        raise ValueError("Lista vazia.")

    if k < 0:
        raise ValueError("Valor de índice inválido.")

    if k >= len(v):
        limit: int = k - len(v)
        for _ in range(limit):
            v.append(0)
        v.append(x)
    else:
        v.insert(k, x)
    return v


def remove(v: list[int], x: int) -> int:
    search_index: int = search(v, x)
    if search_index == -1:
        return -1

    del v[search_index]
    return search_index
