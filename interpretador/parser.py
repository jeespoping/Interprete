import ply.yacc as yacc
import os
from lexer import tokens
import sys

sys.path.insert(0, "../..")
if sys.version_info[0] >= 3:
    raw_input = input

names = {}

precedence = (
    ('left', "PLUS", "MINUS"),
    ('left', "TIMES", "DIVIDE"),
    ('right', 'TIMES'),
)

def p_statement_assign(p):
    'statement : INT ID EQUAL expression SEMICOLON'
    names[p[2]] = p[4]

def p_statement_expr(p):
    'statement : COUT expression SEMICOLON'
    print(p[2])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                      | expression MINUS expression
                      | expression TIMES expression
                      | expression DIVIDE expression'''
    if p[2] == "PLUS":
        p[0] = p[1] + p[3]
    elif p[2] == "MINUS":
        p[0] = p[1] - p[3]
    elif p[2] == "TIMES":
        p[0] = p[1] * p[3]
    elif p[2] == "DIVIDE":
        p[0] = p[1] / p[3]

#def p_expression_uminus(p):
 #   'expression : MINUS expression %prec UMINUS '
  #  p[0] = -P[2]

def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2]

def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]

def p_expression_id(p):
    "expression : ID"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined id '%s'" % p[1])
        p[0] = 0

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

yacc.yacc()

while 1:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)


