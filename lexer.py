import ply.lex as lex

tokens = (
    'VAR', 'LET', 'CONST', 'CLASS', 'FUNCTION', 'TRY', 'CATCH',
    'ID', 'EQUAL', 'NUMBER', 'STRING',
    'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN',
    'COLON', 'COMMA', 'SEMICOLON'
)

reserved = {
    'var': 'VAR',
    'let': 'LET',
    'const': 'CONST',
    'class': 'CLASS',
    'function': 'FUNCTION',
    'try': 'TRY',
    'catch': 'CATCH'
}

t_EQUAL     = r'='
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_COLON     = r':'
t_COMMA     = r','
t_SEMICOLON = r';'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

def t_STRING(t):
    r'\".*?\"'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
