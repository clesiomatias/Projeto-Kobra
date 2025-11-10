import re

# Definição dos tokens
tokens = [
    # Palavras-chave em português (Projeto Kobra)
    ('KEYWORD_PT', r'\b(definir|retornar|se|senao|senaose|para|enquanto|em|nao|e|ou|imprimir|ler|inteiro|flutuante|texto|booleano|intervalo|abrir|fechar|escrever|ler_linha|ler_linhas|tamanho|tipo|lista|dicionario|conjunto|tupla|maximo|minimo|soma|ordenar|reverter|enumerar|filtrar|mapear|qualquer|todos|absoluto|arredondar|potencia|dividir|formato|ajuda|importar|de|como|tentar|exceto|finalmente|levantar|afirmar|com|passar|quebrar|continuar|classe|lambda|global|nonlocal|yield|del|is|Verdadeiro|Falso|Nulo)\b'),
    # Palavras-chave em inglês (Python padrão)
    ('KEYWORD_EN', r'\b(def|return|if|else|elif|for|while|in|not|and|or|print|input|int|float|str|bool)\b'),
    ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z_0-9]*\b'),
    ('NUMBER', r'\b\d+(\.\d+)?\b'),
    ('STRING', r'"[^"]*"|\'[^\']*\''),
    # Operadores compostos primeiro (mais específicos)
    ('OPERATOR', r'==|!=|<=|>=|[\+\-\*/%=<>!&|^]'),
    ('BRACKET', r'[\[\]]'),  # Colchetes
    ('BRACE', r'[\{\}]'),    # Chaves
    ('PARENTHESIS', r'[\(\)]'),
    ('DOT', r'\.'),          # Ponto para acesso a atributos
    ('COMMA', r','),
    ('COLON', r':'),
    ('NEWLINE', r'\n'),      # Quebras de linha (importantes em Python)
    ('INDENT', r'^[ \t]+'),  # Indentação
    ('WHITESPACE', r'[ \t]+'), # Espaços e tabs (exceto quebras de linha)
    ('UNKNOWN', r'.'),
]

# Mapeamento de palavras-chave português -> inglês
keyword_mapping = {
    'definir': 'def',
    'retornar': 'return',
    'se': 'if',
    'senao': 'else',
    'senaose': 'elif',
    'para': 'for',
    'enquanto': 'while',
    'em': 'in',
    'nao': 'not',
    'e': 'and',
    'ou': 'or',
    'imprimir': 'print',
    'ler': 'input',
    'inteiro': 'int',
    'flutuante': 'float',
    'texto': 'str',
    'booleano': 'bool',
    'intervalo': 'range',
    'abrir': 'open',
    'fechar': 'close',
    'escrever': 'write',
    'ler_linha': 'readline',
    'ler_linhas': 'readlines',
    'tamanho': 'len',
    'tipo': 'type',
    'lista': 'list',
    'dicionario': 'dict',
    'conjunto': 'set',
    'tupla': 'tuple',
    'maximo': 'max',
    'minimo': 'min',
    'soma': 'sum',
    'ordenar': 'sorted',
    'reverter': 'reversed',
    'enumerar': 'enumerate',
    'filtrar': 'filter',
    'mapear': 'map',
    'qualquer': 'any',
    'todos': 'all',
    'absoluto': 'abs',
    'arredondar': 'round',
    'potencia': 'pow',
    'dividir': 'divmod',
    'formato': 'format',
    'ajuda': 'help',
    'dir': 'dir',
    'vars': 'vars',
    'globals': 'globals',
    'locals': 'locals',
    'eval': 'eval',
    'exec': 'exec',
    'importar': 'import',
    'de': 'from',
    'como': 'as',
    'tentar': 'try',
    'exceto': 'except',
    'finalmente': 'finally',
    'levantar': 'raise',
    'afirmar': 'assert',
    'com': 'with',
    'passar': 'pass',
    'quebrar': 'break',
    'continuar': 'continue',
    'classe': 'class',
    'lambda': 'lambda',
    'global': 'global',
    'nonlocal': 'nonlocal',
    'yield': 'yield',
    'del': 'del',
    'is': 'is',
    'Verdadeiro': 'True',
    'Falso': 'False',
    'Nulo': 'None'
}

def lexer(code):
    tokens_found = []
    lines = code.split('\n')
    
    for line_num, line in enumerate(lines):
        pos = 0
        # Detecta indentação no início da linha
        indent_match = re.match(r'^[ \t]+', line)
        if indent_match:
            tokens_found.append(('INDENT', indent_match.group(0), line_num + 1))
            pos = indent_match.end()
        
        while pos < len(line):
            match = None
            for token_type, pattern in tokens:
                if token_type == 'INDENT':  # Já processado acima
                    continue
                regex = re.compile(pattern)
                match = regex.match(line, pos)
                if match:
                    token_value = match.group(0)
                    if token_type not in ['WHITESPACE']:
                        # Mapeia palavras-chave portuguesas para inglesas
                        if token_type == 'KEYWORD_PT':
                            english_keyword = keyword_mapping.get(token_value, token_value)
                            tokens_found.append(('KEYWORD', english_keyword, line_num + 1))
                        elif token_type == 'KEYWORD_EN':
                            tokens_found.append(('KEYWORD', token_value, line_num + 1))
                        else:
                            tokens_found.append((token_type, token_value, line_num + 1))
                    pos = match.end()
                    break
            if not match:
                if pos < len(line):
                    raise ValueError(f"Erro léxico na linha {line_num + 1}, posição {pos}: '{line[pos]}'")
                break
        
        # Adiciona quebra de linha se não for a última linha
        if line_num < len(lines) - 1:
            tokens_found.append(('NEWLINE', '\\n', line_num + 1))
    
    return tokens_found

# Exemplo de uso (descomente para testar)
# if __name__ == "__main__":
#     code_example = 'imprimir("Teste do lexer")'
#     tokens = lexer(code_example)
#     for token in tokens:
#         print(token)