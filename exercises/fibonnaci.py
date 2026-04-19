def fibonnaci(n: int) -> str:
    next = 0
    prev = 1
    r = []

    for _ in range(n):
        prev, next = next, prev+next
        r.append(str(prev))

    return "; ".join(r)
