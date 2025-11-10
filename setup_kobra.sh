#!/bin/bash

# Configurar associação de arquivos .kobra para execução direta

echo "🐍 Configurando execução direta de arquivos .kobra..."

# Criar wrapper script
cat > /tmp/kobra-runner << 'EOF'
#!/bin/bash
python3 "$1"
EOF

# Tornar executável
chmod +x /tmp/kobra-runner

# Mover para /usr/local/bin se tiver permissão
if [ -w "/usr/local/bin" ]; then
    sudo mv /tmp/kobra-runner /usr/local/bin/
    echo "✅ Wrapper instalado em /usr/local/bin/kobra-runner"
else
    echo "⚠️  Sem permissão para /usr/local/bin"
    echo "Execute: sudo ./setup_kobra.sh"
fi

# Registrar tipo MIME (opcional)
if command -v xdg-mime &> /dev/null; then
    echo "application/x-kobra" > /tmp/kobra.xml
    echo '<?xml version="1.0" encoding="UTF-8"?>
<mime-info xmlns="http://www.freedesktop.org/standards/shared-mime-info">
  <mime-type type="application/x-kobra">
    <comment>Arquivo Kobra</comment>
    <glob pattern="*.kobra"/>
  </mime-type>
</mime-info>' > /tmp/kobra.xml
    
    xdg-mime install /tmp/kobra.xml
    xdg-mime default kobra-runner application/x-kobra
    echo "✅ Tipo MIME registrado"
fi

echo "Agora você pode executar: python3 arquivo.kobra"