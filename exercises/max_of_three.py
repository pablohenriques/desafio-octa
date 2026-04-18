def verificar_maior(*args):
    maior_numero = -99999999

    for numero in args:
        if numero > maior_numero:
            maior_numero = numero

    return maior_numero
