from datetime import datetime, date
from models import paciente as Paciente
from models.tiposenum import TiposOperacao as status_cad
from userinterfaces.telas_sistema import tela_cadastro_pacientes as telaPacientes
from views import basededados as bd
import models.funcoes as func

titulo_tela = "CADASTRO DE PACIENTES".center(73, " ")

def exibir_tela_cadastro():
    pass

def get_campo_int(linha: int, coluna: int, campo: str):
    valor_ok = False
    result = 0
    while not valor_ok:
        try:
            func.posicionarCursor(linha, coluna)
            result = int(input())
            valor_ok = True
        except ValueError:
            func.exibirMensagem(29, 3, f"Valor inválido para {campo}.")
            input()
    return result

def exibir_dados_paciente(paciente: Paciente):
    func.posicionarCursor(6, 72)
    print(f"{paciente.data_nasc.strftime("%d/%m/%Y")}")

def digitar_dados_paciente():
    pass

def iniciar():
    func.limpar_linha(29, 2, 95)
    func.desenhar_tela(6, 3, telaPacientes, len(telaPacientes) - 1, 26)

    opcao = ""

    while opcao != "S":
        num_cpf = get_campo_int(6, 14, "CPF")
        paciente, erro = bd.buscar_paciente(num_cpf)
        if paciente:
            exibir_dados_paciente(paciente)
        digitar_dados_paciente()
