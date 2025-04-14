from models import paciente as Paciente
from models import historico as Historico
from models.tiposenum import TiposOperacao as statusCad
from models.funcoes import exibirMensagem as showMessage

listaPacientes = dict()
listaHistoricos = dict()

def manutencao_paciente(paciente: Paciente, tipoOperacao: statusCad):
    try:
        if tipoOperacao == statusCad.INCLUSAO or tipoOperacao == statusCad.ALTERACAO:
            listaPacientes[paciente.num_cpf] = paciente
        elif tipoOperacao == statusCad.EXCLUSAO:
            del listaPacientes[paciente.num_cpf]
        return True, "Operação efetuada com sucesso!"
    except Exception as ex: 
        if len(ex) > 87:
            ex = ex[:87]
        return False, ex
    
def buscar_paciente(num_cpf: int):
    paciente = listaPacientes.get(num_cpf)
    if paciente:
        return paciente, None
    else:
        return None, "Paciente não encontrado"