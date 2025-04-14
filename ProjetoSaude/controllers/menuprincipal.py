from os import system as limp
from datetime import datetime
import locale
import models.funcoes as func
from userinterfaces.telas_sistema import tela_principal as telaPrinc
from userinterfaces.telas_sistema import opcoes_principais as opcoesPrincipais

locale.setlocale(locale.LC_TIME, "Portuguese_Brazil.1252")
titulo_principal = "LABORATÓRIO DE ANÁLISES CLINICAS - Dr. André Rogério Bononi"
data_atual = f"Data: {datetime.now().strftime("%a")} - {datetime.now().strftime("%d/%m/%Y")}"

def exibir_tela_principal():
    limp("cls")
    print(telaPrinc)
    func.posicionarCursor(3, 3)
    print(titulo_principal, end="")
    func.posicionarCursor(3, 74)
    print(data_atual, end="")
    exibir_opcoes_principais()

def exibir_opcoes_principais():
    func.limpar_tela(5, 28, 2, 95)
    linha = 6
    indice_final = len(opcoesPrincipais)
    indice = 1
    for opcao in opcoesPrincipais:
        if indice == indice_final:
            linha = 23
        func.posicionarCursor(linha, 3)
        print(opcao, end="")
        linha +=1
        indice += 1

def iniciar():
    opcao = 0
    exibir_tela_principal()
    
    while opcao != 9:
        try:
            func.posicionarCursor(26, 3)
            print("Escolha a opção desejada: [ ]")
            func.posicionarCursor(26, 30)
            opcao = int(input())
            if (opcao == 9):
                break;
            
        except ValueError:
            func.exibirMensagem(29, 3, "Valor inválido. Escolha um dos disponíveis")
            input()
            func.limpar_linha(29, 2, 95)
