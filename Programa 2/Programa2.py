import re

simbolos = {'*': {
    'name': 'Operador de Multiplicação',
    'found': False
},
    '/': {
    'name': 'Operador de Divisão',
    'found': False
},
    '+': {
    'name': 'Operador de Adição',
    'found': False
},
    '-': {
    'name': 'Operador de Subtração',
    'found': False
},
    '=': {
    'name': 'Operador de Atribuição',
    'found': False
},
    '^': {
    'name': 'Operador de Expoente',
    'found': False
},
    ';': {
    'name': 'Delimitador',
    'found': False
},
    'if': {
    'name': 'Estrutura Condicional',
    'found': False
},
    'else': {
    'name': 'Estrutura Condicional',
    'found': False
},
    'int': {
    'name': 'Tipo Inteiro',
    'found': False
}, 'float': {
    'name': 'Tipo Decimal',
    'found': False
},
    'double': {
    'name': 'Tipo Decimal',
    'found': False
},
    'char': {
    'name': 'Estrutura Condicional',
    'found': False
},
    '[': {
    'name': 'Identificador Abre Vetor',
    'found': False
},
    ']': {
    'name': 'Identificador Fecha Vetor',
    'found': False
},
'(': {
    'name': 'Identificador Abre Chamada Funcao',
    'found': False
},
    ')': {
    'name': 'Identificador Fecha Chamada Funcao',
    'found': False
},
'{': {
    'name': 'Identificador Abre Escopo',
    'found': False
},
    '}': {
    'name': 'Identificador Fecha Escopo',
    'found': False
},
'"': {
    'name': 'Identificador Abre/Fecha Aspas',
    'found': False
},
    'return': {
    'name': 'Retorno de funcao',
    'found': False
}
}


def is_float(s: str):
    try:
        float(s)
        return True
    except ValueError:
        return False


def removeComments(codigo: str):
    codigo = re.sub(re.compile("/\*.*?\*/", re.DOTALL), "", codigo)
    codigo = re.sub(re.compile("//.*?\n"), "", codigo)
    print('\nCodigo sem comentarios:\n')
    print(codigo)
    return codigo


def imprimeTabela(linha: str):
    identificador = 0
    print("\nLexemas encontrados | Token (Tipo de token)")
    for char in linha.split():
        if char != ' ':
            if char in simbolos:
                if not simbolos[char]['found']:
                    print("{} | {}".format(char, simbolos[char]['name']))
                    simbolos[char]['found'] = True
            elif is_float(char):
                print("{} | Numero".format(char))
                simbolos[char] = {
                    'name': "Numero",
                    'found': True
                }
            else:
                identificador += 1
                print("{} | Identificador {}".format(char, identificador))
                simbolos[char] = {
                    'name': "Identificador {}".format(identificador),
                    'found': True
                }
    print("\n")


def main():
    codigo_c_1 = '''
    // Minha funcao main
        int main ( )
        {
          /*Meu outro comentario*/
            int result ;
            float vector [ ] ;
            if ( result != 0 ) { 
                vector [ 0 ] = 10.90 ;
                printf_s ( result ) ;
            }
            // Meu ultimo comentario no meu retorno
            return 10 ;
        }
  '''
    codigo_c_2 = '''
    // Minha funcao main
    int main() {
    float x = 10.327 ;
    double y = 4244.546 ;
    /*Meu outro comentario*/
    int z = 28 ;
    float soma = x + y + z ;
   // Imprimindo valores
    printf ( soma ) ;

    return 0 ;
}
  '''
    linhaSemComentario = removeComments(codigo_c_2)
    imprimeTabela(linhaSemComentario)


main()
