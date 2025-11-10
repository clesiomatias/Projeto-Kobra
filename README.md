# 🐍 Projeto Kobra

**Transformando o aprendizado de programação com Python em português.**

## 📌 Índice

* [Descrição](#descrição)
* [Objetivo](#objetivo)
* [Instalação](#instalação)
* [Como Usar](#como-usar)
* [Funcionalidades Implementadas](#funcionalidades-implementadas)
* [Exemplos de Uso](#exemplos-de-uso)
* [IDE e Extensões](#ide-e-extensões)
* [Como Contribuir](#como-contribuir)
* [Licença](#licença)
* [Contato](#contato)

---

## 🧠 Descrição

O **Projeto Kobra** visa adaptar a linguagem de programação Python para o português, facilitando o aprendizado de programação para falantes nativos da língua. O projeto oferece um interpretador completo que traduz comandos em português para Python.

---

## 🎯 Objetivo

* **Educação**: Proporcionar uma ferramenta de ensino que utilize uma linguagem mais próxima da realidade dos alunos.
* **Acessibilidade**: Reduzir a barreira linguística no aprendizado de programação.
* **Evolução Contínua**: Expandir o projeto conforme o feedback dos usuários e as necessidades educacionais.

---

## 🚀 Instalação

### Requisitos
- Python 3.6+
- Sistema Linux/macOS/Windows

### Instalação Rápida
```bash
git clone https://github.com/seuprojeto/projeto-kobra.git
cd projeto-kobra
chmod +x kobra.py
```

### Instalação Global (Opcional)
```bash
./install.sh  # ou sudo ./install.sh
```

---

## 💻 Como Usar

### Executar arquivo .kobra
```bash
# Método 1: Usando o interpretador
python3 kobra.py arquivo.kobra

# Método 2: Execução direta (com shebang)
python3 arquivo.kobra

# Método 3: Após instalação global
kobra arquivo.kobra
```

### IDE Simples
```bash
python3 ide_simples.py
```

---

## ⚙️ Funcionalidades Implementadas

### 🎯 Comandos Básicos
| Português | Python | Status | Descrição |
|-----------|--------|--------|-----------|
| `imprimir()` | `print()` | ✅ | Exibe saídas no console |
| `ler()` | `input()` | ✅ | Lê entrada do usuário |
| `tamanho()` | `len()` | ✅ | Retorna tamanho de objeto |
| `tipo()` | `type()` | ✅ | Retorna tipo do objeto |

### 🔢 Funções Matemáticas
| Português | Python | Status | Descrição |
|-----------|--------|--------|-----------|
| `soma()` | `sum()` | ✅ | Soma elementos de lista |
| `maximo()` | `max()` | ✅ | Valor máximo |
| `minimo()` | `min()` | ✅ | Valor mínimo |
| `absoluto()` | `abs()` | ✅ | Valor absoluto |
| `arredondar()` | `round()` | ✅ | Arredonda número |
| `potencia()` | `pow()` | ✅ | Potenciação |

### 📊 Estruturas de Dados
| Português | Python | Status | Descrição |
|-----------|--------|--------|-----------|
| `lista` | `list` | ✅ | Lista/array |
| `dicionario` | `dict` | ✅ | Dicionário |
| `conjunto` | `set` | ✅ | Conjunto |
| `tupla` | `tuple` | ✅ | Tupla |
| `intervalo()` | `range()` | ✅ | Sequência numérica |

### 🔄 Controle de Fluxo
| Português | Python | Status | Descrição |
|-----------|--------|--------|-----------|
| `se` | `if` | ✅ | Condicional |
| `senao` | `else` | ✅ | Alternativa |
| `senaose` | `elif` | ✅ | Condicional múltipla |
| `para` | `for` | ✅ | Loop |
| `enquanto` | `while` | ✅ | Loop condicional |
| `quebrar` | `break` | ✅ | Interrompe loop |
| `continuar` | `continue` | ✅ | Pula iteração |

### 🏗️ Definições
| Português | Python | Status | Descrição |
|-----------|--------|--------|-----------|
| `definir` | `def` | ✅ | Define função |
| `classe` | `class` | ✅ | Define classe |
| `retornar` | `return` | ✅ | Retorna valor |
| `passar` | `pass` | ✅ | Comando vazio |

### 🔍 Operadores Lógicos
| Português | Python | Status | Descrição |
|-----------|--------|--------|-----------|
| `e` | `and` | ✅ | E lógico |
| `ou` | `or` | ✅ | OU lógico |
| `nao` | `not` | ✅ | NÃO lógico |
| `em` | `in` | ✅ | Pertencimento |
| `is` | `is` | ✅ | Identidade |

### 📄 Valores Especiais
| Português | Python | Status | Descrição |
|-----------|--------|--------|-----------|
| `Verdadeiro` | `True` | ✅ | Valor verdadeiro |
| `Falso` | `False` | ✅ | Valor falso |
| `Nulo` | `None` | ✅ | Valor nulo |

### 🔧 Tipos de Dados
| Português | Python | Status | Descrição |
|-----------|--------|--------|-----------|
| `inteiro` | `int` | ✅ | Número inteiro |
| `flutuante` | `float` | ✅ | Número decimal |
| `texto` | `str` | ✅ | String/texto |
| `booleano` | `bool` | ✅ | Verdadeiro/Falso |

---

## 📝 Exemplos de Uso

### Função `imprimir()`
```python
# Texto simples
imprimir("Olá, mundo!")

# Múltiplos parâmetros
imprimir("Projeto", "Kobra", "em", "ação!")

# Com variáveis
nome = "Python"
linguagem = "Kobra"
imprimir("Traduzindo", nome, "para", linguagem)

# Com números
idade = 25
imprimir("Idade:", idade)
```

### Estruturas de Controle
```python
# Condicional
idade = 18
se idade >= 18:
    imprimir("Maior de idade")
senao:
    imprimir("Menor de idade")

# Loop
para i em intervalo(5):
    imprimir("Número:", i)

# While
contador = 0
enquanto contador < 3:
    imprimir("Contador:", contador)
    contador = contador + 1
```

### Funções
```python
# Definir função
definir saudacao(nome):
    retornar "Olá, " + nome + "!"

# Usar função
mensagem = saudacao("Mundo")
imprimir(mensagem)
```

### Listas e Operações
```python
# Lista
numeros = [1, 2, 3, 4, 5]
frutas = ["maçã", "banana", "laranja"]

# Operações
imprimir("Tamanho:", tamanho(numeros))
imprimir("Soma:", soma(numeros))
imprimir("Máximo:", maximo(numeros))
imprimir("Mínimo:", minimo(numeros))

# Loop em lista
para fruta em frutas:
    imprimir("Fruta:", fruta)
```

### Dicionários
```python
# Dicionário
pessoa = {"nome": "Ana", "idade": 30}
imprimir("Nome:", pessoa["nome"])
imprimir("Idade:", pessoa["idade"])
```

---

## 🛠️ IDE e Extensões

### Plugin VS Code
O Projeto Kobra inclui uma extensão completa para VS Code:

**Funcionalidades:**
- ✅ Syntax highlighting para arquivos `.kobra`
- ✅ Execução com `Ctrl+F5`
- ✅ Ícone personalizado para arquivos `.kobra`
- ✅ Auto-indentação e comentários

**Instalação:**
```bash
cd vscode-extension
./build.sh
code --install-extension kobra-language-*.vsix
```

### IDE Simples
IDE dedicada com interface gráfica:
```bash
python3 ide_simples.py
```

**Funcionalidades:**
- ✅ Editor com syntax básico
- ✅ Execução integrada (F5)
- ✅ Menu completo (Novo, Abrir, Salvar)
- ✅ Painel de saída

---

## 🧪 Testes

### Executar testes unitários
```bash
python3 test_imprimir.py
```

### Arquivos de exemplo
- `exemplo_puro.kobra` - Comandos básicos
- `exemplo_completo.kobra` - Funcionalidades avançadas
- `teste_comandos.kobra` - Teste de comandos individuais

---

## 🤝 Como Contribuir

1. **Fork** este repositório
2. Crie uma **branch** para sua contribuição:
   ```bash
   git checkout -b minha-contribuicao
   ```
3. Realize as alterações desejadas
4. **Commit** suas mudanças:
   ```bash
   git commit -am 'Adiciona nova funcionalidade'
   ```
5. Envie para o repositório remoto:
   ```bash
   git push origin minha-contribuicao
   ```
6. Abra um **Pull Request** explicando suas alterações

Todas as contribuições são bem-vindas!

---

## ✅ Etapas Concluídas

| Etapa | Status | Observações |
|-------|--------|-------------|
| Analisador Léxico | ✅ | Reconhece todos os comandos em português |
| Analisador Sintático | ✅ | Converte para AST Python |
| Interpretador | ✅ | Executa código Kobra |
| Função `imprimir()` | ✅ | Implementada e testada |
| Comandos básicos | ✅ | 60+ comandos traduzidos |
| Plugin VS Code | ✅ | Extensão completa |
| IDE Simples | ✅ | Interface gráfica funcional |
| Testes unitários | ✅ | Cobertura básica |
| Documentação | ✅ | README completo |

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE]() para mais detalhes.

---

## 📬 Contato

Para dúvidas ou sugestões, entre em contato:

* **E-mail**: [clesiofmatias@gmail.com]()
* **GitHub**: [@clesiomatias](https://github.com/clesiomatias)

---

## 🌟 Apoie o Projeto

Se o Projeto Kobra foi útil para você, considere:
- ⭐ Dar uma estrela no repositório
- 🐛 Reportar bugs ou sugerir melhorias
- 🤝 Contribuir com código
- 📢 Compartilhar com outros educadores

**Juntos, tornamos a programação mais acessível em português!** 🇧🇷🐍