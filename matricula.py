import os
import sys
import time

textoMenu = """
1 - Matricular Novo Aluno
2 - Remover Aluno
3 - Listar Alunos Matriculados
4 - Modificar Dados do  Aluno
5 - Sair
"""
def menu():
   os.system("clear")
   print(textoMenu)

Lista_Alunos = []
while(True):
 menu()
 opcao = input("Escolha ..: ")
 if opcao =="1":
     aluno = input("Digite um nome..:")
     Lista_Alunos.append(aluno)
     print("opcao 1 acionada")
     time.sleep(2)
 if opcao =="2":
     aluno = input("Digite um nome..:")
     Lista_Alunos.remove(aluno)
     print("opcao 2 acionada")
     time.sleep(2)
 if opcao =="3":
     for aluno in Lista_Alunos:
        print(aluno)
     time.sleep(2)
 if opcao =="5":
   print("Good Bye")
   sys.exit(0)
