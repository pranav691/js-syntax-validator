import ply.yacc as yacc
from lexer import tokens

def p_variable(p):
    '''statement : VAR ID EQUAL value SEMICOLON
                 | LET ID EQUAL value SEMICOLON
                 | CONST ID EQUAL value SEMICOLON'''
    pass

def p_value(p):
    '''value : NUMBER
             | STRING
             | ID
             | object'''
    pass

def p_object(p):
    '''object : LBRACE key_value_pairs RBRACE
              | LBRACE RBRACE'''
    pass

def p_key_value_pairs(p):
    '''key_value_pairs : STRING COLON value
                       | STRING COLON value COMMA key_value_pairs'''
    pass

def p_function(p):
    '''statement : FUNCTION ID LPAREN RPAREN LBRACE RBRACE'''
    pass

def p_class(p):
    '''statement : CLASS ID LBRACE RBRACE'''
    pass

def p_trycatch(p):
    '''statement : TRY LBRACE RBRACE CATCH LPAREN ID RPAREN LBRACE RBRACE'''
    pass

def p_error(p):
    raise SyntaxError

parser = yacc.yacc()
