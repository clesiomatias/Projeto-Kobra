#!/usr/bin/env python3
import sys
import os
from interpretador import InterpretadorKobra

def main():
    if len(sys.argv) != 2:
        print("Uso: python kobra.py arquivo.kobra")
        sys.exit(1)
    
    arquivo = sys.argv[1]
    
    if not os.path.exists(arquivo):
        print(f"Erro: Arquivo '{arquivo}' não encontrado.")
        sys.exit(1)
    
    if not arquivo.endswith('.kobra'):
        print("Aviso: Arquivo não possui extensão .kobra")
    
    interpretador = InterpretadorKobra()
    interpretador.executar_arquivo(arquivo)

if __name__ == "__main__":
    main()