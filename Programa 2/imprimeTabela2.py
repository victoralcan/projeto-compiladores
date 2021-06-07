simbolos = {'*': 'Operador de Multiplicação',
'/': 'Operador de Divisão',
'+': 'Operador de Adição',
'-': 'Operador de Subtração',
'=': 'Operador de Atribuição',
'^': 'Operador de Expoente',
';': 'Delimitador'
}

def imprimeTabela(linha: str):
  identificador = 0
  print("Lexema | Token (Tipo de token)")
  for char in linha.split(): 
    if char != ' ':
      if char in simbolos:
        print("{} | {}".format(char, simbolos[char]))
      elif char.isdigit():
        print("{} | Numero".format(char))
      else:
        identificador += 1
        print("{} | Identificador {}".format(char, identificador))

def checkIsValid():
  linha = input("Digite uma linha de três operandos e no maximo dois operadores além do de atribuição: ")
  previous = ''
  listaLinha = linha.split();
  operandos = 0
  operadores = 0
  operadorAtribuicao = 0
  for char in listaLinha:
    if char in simbolos:
      if char == '=' and operadorAtribuicao == 0:
        operadorAtribuicao = 1
      elif char == '=' and operadorAtribuicao == 1:
        print('\nFoi encontrado mais de um operador de atribuição!\n')
        return

      operadores += 1

      if operadores > 2:
        print("\nApenas são permitidos dois operadores além do de atribuição\n")
        return
      if previous == 'operador':
        print("\nForam encontrados dois operadores seguidos\n")
        return
      else:
        previous = 'operador'
    elif char.isdigit():
      operandos += 1
      if previous == 'numero':
        print("\nForam encontrados dois numeros seguidos\n")
        return
      else: 
        previous = 'numero'
    else:
      operandos += 1
      if previous == 'identificador':
        print("\nForam encontrados dois identificadores seguidos\n")
        return
      else: 
        previous = 'identificador'    
    if operandos > 3:
      print("\nApenas são permitidos dois operandos\n")
      return
    
  imprimeTabela(linha)

checkIsValid()
