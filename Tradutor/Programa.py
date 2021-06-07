import sys
sys.tracebacklimit=0
class Node():
    def __init__(self, valor, prox = None):
        self.valor = valor
        self.prox = prox

    def __str__(self):
        return str(self.valor)
def operacao(op, opnd1, opnd2):
    if op == "+":
        return opnd1 + opnd2
    elif op == "-":
        return opnd1 - opnd2
    elif op == "*":
        return opnd1 * opnd2
    elif op == "/":
        return opnd1 / opnd2
    elif op == "$":
        return opnd1 ** opnd2
    else:
        return False                # Retorna False caso o operando não seja válido

def avaliarPosfixa(expressao):
    """ Avalia uma expressao posfixa"""
    p = Pilha()
    for i in range(len(expressao)):
        c = expressao[i]
        if c >= "0" and c <= "9":
            p.push(c)
        else:
            opnd2 = p.pop()
            opnd1 = p.pop()

            valor = operacao(c, int(opnd1), int(opnd2))

            if valor:                                       # Verifica se o operando é válido   
                p.push(valor)
            else:
                return "Operador invalido"
    
    resultado = p.pop()

    if p.isEmpty():                 # Verifica se ao final a pilha está vazia
        return resultado
    else:
        return "Expressao invalida"



def isOperador(s):
    if s == "+" or s == "-" or s == "*" or s == "/" or s == "$":
        return True
    else:
        return False

def prioridade(c, t):
    """Verifica a prioridade entre os operandos"""
    if c == '$':
        pc = 4
    elif c == '*' or c == '/':
        pc = 2
    elif c == '+' or c == '-':
        pc = 1
    else:
        pc = 4
 
    if t == '$':
        pt = 3
    elif t == '*' or t == '/':
        pt = 2
    elif t == '+' or t == '-':
        pt = 1
    else:
        pt = 0

    return pc <= pt

def postfix(infix):
    """Converte uma expressao infixa em posfixa"""

    p = Pilha()
    posfixa = []

    for i in range(len(infix)):
        c = infix[i]
        if c >= '0' and c <= '9' or c.lower() >= 'a' and c.lower() <= 'z':
            posfixa.append(c)
        elif isOperador(c):
            while not p.isEmpty() and prioridade(c, p.stacktop()):
                t = p.pop()
                posfixa.append(t)
            p.push(c)
        elif c == '(':
            p.push(c)
        elif c == ')':
            while True:
                t = p.pop()
                if t != '(':
                    posfixa.append(t)
                else:
                    break
    while not p.isEmpty():
        posfixa.append(p.pop())

    posfixa = "".join(posfixa)

    return posfixa

class Pilha():
    def __init__(self):
        self.topo = None
        self.cont = 0

    def __str__(self):
        strPilha = ""
        node = self.topo
        while True:
            strPilha += str(node.valor) + "\n"
            node = node.prox
            if node == None:
                break
        return strPilha

    def isEmpty(self):
        if self.topo == None:
            return True
        else:
            return False

    def push(self, v):
        if self.isEmpty():
            self.topo = Node(v)
            self.cont += 1
        else:
            novo = Node(v, self.topo)
            self.topo = novo
            self.cont += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Pilha vazia")
        v = self.topo.valor
        self.topo = self.topo.prox
        self.cont -= 1
        return v

    def stacktop(self):
        if self.isEmpty():
            raise Exception("Pilha vazia")
        return self.topo.valor 

infixa = input("Digite uma expressao infixa: ")

try:
  posfixa = postfix(infixa)

  print("\nExpressao infixa: {0} \nExpressao posfixa: {1}".format(infixa, posfixa))

  resultado = avaliarPosfixa(posfixa)

  print("Resultado: {0}\n".format(resultado))

except:
  exit();
