from unittest import TestCase, main

def verificar_maior(*args):
    maior_numero = -99999999

    for numero in args:
        if numero > maior_numero:
            maior_numero = numero
    
    return maior_numero

class TestMaiorNumero(TestCase):

    def test_caso_01(self):
        resultado = verificar_maior(10, 5, 1)
        self.assertEqual(resultado, 10)

    def test_caso_02(self):
        resultado = verificar_maior(-1, -5, -4)
        self.assertEqual(resultado, -1)




if __name__ == "__main__":
    main()

