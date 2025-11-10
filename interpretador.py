import ast
from analisador_lexico import lexer
from analisador_sintatico import AnalisadorSintatico

class InterpretadorKobra:
    def __init__(self):
        self.globals = {}
        self.locals = {}
    
    def executar(self, codigo_kobra):
        """Executa código em português do Projeto Kobra"""
        try:
            # Análise léxica
            tokens = lexer(codigo_kobra)
            
            # Análise sintática
            parser = AnalisadorSintatico(tokens)
            python_code = parser._tokens_to_python()
            
            # Execução
            exec(python_code, self.globals, self.locals)
            
        except Exception as e:
            print(f"Erro na execução: {e}")
    
    def executar_arquivo(self, caminho_arquivo):
        """Executa arquivo .kobra"""
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            codigo = arquivo.read()
        self.executar(codigo)

# Função principal para testar
if __name__ == "__main__":
    interpretador = InterpretadorKobra()
    
    # Teste da função imprimir
    codigo_teste = '''
imprimir("Olá, mundo!")
imprimir("Teste com múltiplos", "parâmetros", 123)
nome = "Kobra"
imprimir("Projeto", nome)
'''
    
    print("=== Executando código Kobra ===")
    interpretador.executar(codigo_teste)