import re

def removeComments(codigo: str):
    codigo = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,codigo) 
    codigo = re.sub(re.compile("//.*?\n" ) ,"" ,codigo)
    print(codigo)

cod = input("Digite o código a ser limpo: ")

removeComments(cod)