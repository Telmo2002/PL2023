import ply.lex as lex

tokens = (
    'INT',
    'VAR',
    'PONTOEVIRGULA',
    'FUNCAO',
    'NOMEFUNCAO',
    'ABRIRPARENTISES',
    'FECHARPARENTISES',
    'ARGUMENTO',
    'VIRGULA',
    'ABRIRCHAVETA',
    'FECHARCHAVETA',
    'IGUAL',
    'NUMERO',
    'WHILE',
    'COMPARADORES',
    'OPERADORES',
    'PROGRAMA',
    'FOR',
    'IN',
    'RANGE',
    'IF',
    'ABRIRPARENTISESRETO',
    'FECHARPARENTISESRETO'
)

def t_ignore_COMENTARIODEUMALINHA(t):
    r'\/\/.*?\n'
    pass

def t_ignore_COMENTARIOVARIASLINHAS(t):
    r'\/\*(.|\n)*?\*\/'
    pass

def t_INT(t):
    r'int'
    return t

def t_PROGRAMA(t):
    r'program\s\w+'
    return t

def t_PONTOEVIRGULA(t):
    r'\;'
    return t

def t_FUNCAO(t):
    r'function '
    return t

def t_NOMEFUNCAO(t):
    r'\w+(?=\()'
    return t

def t_ABRIRPARENTISES(t):
    r'\('
    return t

def t_FECHARPARENTISES(t):
    r'\)'
    return t

def t_ARGUMENTO(t):
    r'[A-Za-z]+\w*(?=\)|\,)'
    return t

def t_VIRGULA(t):
    r'\,'
    return t

def t_RANGE(t):
    r'\[\d+\.\.\d+\]'
    return t

def t_ABRIRCHAVETA(t):
    r'\{'
    return t
def t_FECHARCHAVETA(t):
    r'\}'
    return t

def t_IGUAL(t):
    r'\='
    return t

def t_NUMERO(t):
    r'[+-]?\d+'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_COMPARADORES(t):
    r'(<|>|==|>=|<=)'
    return t

def t_OPERADORES(t):
    r'(\+|\-|\*|\/)'
    return t

def t_FOR(t):
    r'for'
    return t

def t_IN(t):
    r'in'
    return t


def t_IF(t):
    r'if'
    return t

def t_ABRIRPARENTISESRETO(t):
    r'\['
    return t

def t_FECHARPARENTISESRETO(t):
    r'\]'
    return t

def t_VAR(t):
    r'\w+'
    return t

t_ignore=' \t\n'

def t_error(t):
    print(f"Caracter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

function1 = '''
/* factorial.p
-- 2023-03-20 
-- by jcr
*/
int i;
// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}
// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}
'''

function2 = '''
/* max.p: calcula o maior inteiro duma lista desordenada
-- 2023-03-20 
-- by jcr
*/
int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};
// Programa principal
program myMax{
  int max = a[0];
  for i in [1..9]{
    if max < a[i] {
      max = a[i];
    }
  }
  print(max);
}
'''

lexer.input(function1)

while tok := lexer.token():
    print(tok)