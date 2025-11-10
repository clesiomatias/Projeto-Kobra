#!/bin/bash

echo "🔨 Construindo extensão Kobra para VS Code..."

# Instalar dependências
npm install

# Compilar TypeScript
npm run compile

# Instalar vsce se não existir
if ! command -v vsce &> /dev/null; then
    npm install -g vsce
fi

# Criar pacote VSIX
vsce package

echo "✅ Extensão criada! Para instalar:"
echo "code --install-extension kobra-language-*.vsix"