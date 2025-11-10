#!/bin/bash

# Script de instalação do Projeto Kobra

echo "🐍 Instalando Projeto Kobra..."

# Criar link simbólico para executar arquivos .kobra globalmente
INSTALL_DIR="/usr/local/bin"
SCRIPT_PATH="$(pwd)/kobra.py"

if [ -w "$INSTALL_DIR" ]; then
    ln -sf "$SCRIPT_PATH" "$INSTALL_DIR/kobra"
    echo "✅ Kobra instalado em $INSTALL_DIR/kobra"
    echo "Agora você pode executar: kobra arquivo.kobra"
else
    echo "⚠️  Sem permissão para instalar em $INSTALL_DIR"
    echo "Execute: sudo ./install.sh"
    echo "Ou use: python3 kobra.py arquivo.kobra"
fi