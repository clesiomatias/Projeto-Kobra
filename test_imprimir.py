import unittest
import sys
from io import StringIO
from interpretador import InterpretadorKobra

class TestImprimir(unittest.TestCase):
    def setUp(self):
        self.interpretador = InterpretadorKobra()
        self.output = StringIO()
        sys.stdout = self.output
    
    def tearDown(self):
        sys.stdout = sys.__stdout__
    
    def test_imprimir_texto_simples(self):
        """Testa impressão de texto simples"""
        codigo = 'imprimir("Olá, mundo!")'
        self.interpretador.executar(codigo)
        self.assertEqual(self.output.getvalue().strip(), "Olá, mundo!")
    
    def test_imprimir_multiplos_parametros(self):
        """Testa impressão com múltiplos parâmetros"""
        codigo = 'imprimir("Teste", "múltiplos", "parâmetros")'
        self.interpretador.executar(codigo)
        self.assertEqual(self.output.getvalue().strip(), "Teste múltiplos parâmetros")
    
    def test_imprimir_numeros(self):
        """Testa impressão de números"""
        codigo = 'imprimir(123, 45.67)'
        self.interpretador.executar(codigo)
        self.assertEqual(self.output.getvalue().strip(), "123 45.67")
    
    def test_imprimir_variaveis(self):
        """Testa impressão de variáveis"""
        codigo = '''
nome = "Kobra"
versao = 1.0
imprimir("Projeto", nome, "versão", versao)
'''
        self.interpretador.executar(codigo)
        self.assertEqual(self.output.getvalue().strip(), "Projeto Kobra versão 1.0")
    
    def test_imprimir_quebra_linha(self):
        """Testa se adiciona quebra de linha"""
        codigo = '''
imprimir("Linha 1")
imprimir("Linha 2")
'''
        self.interpretador.executar(codigo)
        linhas = self.output.getvalue().strip().split('\n')
        self.assertEqual(len(linhas), 2)
        self.assertEqual(linhas[0], "Linha 1")
        self.assertEqual(linhas[1], "Linha 2")

if __name__ == '__main__':
    unittest.main()