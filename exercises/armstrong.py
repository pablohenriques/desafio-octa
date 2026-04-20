def armstrong(x: int) -> bool: return x == sum([pow(int(n), len(str(x))) for n in str(x)])

def armstrong_until(n):
    return [x for x in range(1, n+1) if armstrong(x)]