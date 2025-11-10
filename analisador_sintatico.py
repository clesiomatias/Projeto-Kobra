import ast
from analisador_lexico import lexer, keyword_mapping

class AnalisadorSintatico:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    
    def parse(self):
        """Converte tokens em AST Python válida"""
        python_code = self._tokens_to_python()
        return ast.parse(python_code)
    
    def _tokens_to_python(self):
        """Converte tokens para código Python padrão"""
        python_tokens = []
        
        for i, token in enumerate(self.tokens):
            if len(token) == 3:
                token_type, value, line = token
            else:
                token_type, value = token
                line = 1
            
            if token_type == 'KEYWORD':
                python_tokens.append(value)
                # Adicionar espaço após keywords se próximo token não for parênteses/dois pontos
                if i + 1 < len(self.tokens):
                    next_token = self.tokens[i + 1]
                    next_type = next_token[0] if len(next_token) >= 1 else ''
                    if next_type not in ['PARENTHESIS', 'COLON']:
                        python_tokens.append(' ')
            elif token_type == 'NEWLINE':
                python_tokens.append('\n')
            elif token_type == 'INDENT':
                python_tokens.append(value)
            elif token_type == 'OPERATOR':
                python_tokens.append(' ' + value + ' ')
            elif token_type != 'WHITESPACE':
                python_tokens.append(value)
        
        return ''.join(python_tokens)