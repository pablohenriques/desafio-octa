def max_of_three(numeros: list[int]) -> int:
    if not numeros:
        raise ValueError("A lista está vazia")

    maior_numero = numeros[0]
    for numero in numeros[1:]:
        if numero > maior_numero:
            maior_numero = numero

    return maior_numero
