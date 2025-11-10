#!/usr/bin/env python3
from analisador_lexico import lexer
from analisador_sintatico import AnalisadorSintatico

# Debug do arquivo problemático
with open('teses_bobos.kobra', 'r', encoding='utf-8') as f:
    codigo = f.read()

print("=== CÓDIGO ORIGINAL ===")
print(codigo)

print("\n=== TOKENS ===")
tokens = lexer(codigo)
for i, token in enumerate(tokens):
    print(f"{i}: {token}")

print("\n=== CÓDIGO PYTHON GERADO ===")
parser = AnalisadorSintatico(tokens)
python_code = parser._tokens_to_python()
print(repr(python_code))
print("\n" + python_code)