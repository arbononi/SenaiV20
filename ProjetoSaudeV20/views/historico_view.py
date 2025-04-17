import msvcrt
from datetime import datetime, date
from views.layout_telas import layout_historico, layout_rel_historicos
from models.tiposenum import TiposTemperatura, TiposPressaoArterial, TiposFrequenciaCardiaca, TiposAtendimento
from utils import user_functions, constantes
from utils.user_functions import esperar_tecla, formatar_data_hora, formatar_cpf, formatar_data, posicionarCursor
from models.tiposenum import TiposOperacao as status_cad
from models.historico import Historico
from models.paciente import Paciente
from database import basedados

campos_historico = {
    "id": {"line": 7, "column" : 14, "size": 15},
    "data_exame": {"line": 7, "column" : 81, "size": 10},
    "num_cpf": {"line": 8, "column" : 14, "size": 14},
    "data_nasc" : {"line": 8, "column" : 74, "size": 10},
    "idade" : {"line": 8, "column" : 94, "size": 3},
    "nome_paciente" : {"line": 9, "column" : 14, "size": 83},
    "temperatura" : {"line": 14, "column" : 19,  "size": 5},
    "pressao_arterial" : {"line": 14, "column" : 56,  "size": 5},
    "frequencia_cardiaca": {"line": 14, "column" : 91,  "size": 3}
}

campos_tipo_temperatura = {
    "HIPOTERMIA" : {"line" : 19, "column" : 6, "size": 1},
    "NORMAL" : {"line" : 20, "column" : 6, "size" : 1},
    "FEBRE_LEVE" : {"line" : 21, "column" : 6, "size" : 1},
    "FEBRE_ALTA" : {"line" : 22, "column" : 6, "size": 1}
}

campos_tipo_pressao_arterial = {
    "BAIXA" : {"line" : 19, "column" : 38, "size" : 1},
    "NORMAL" : {"line" : 20, "column" : 38, "size" : 1},
    "ALTA" : {"line" : 21, "column" : 38, "size" : 1}
}

campos_tipo_frequencia_cardiaca = {
    "BRAQUICARDIA" : {"line" : 19, "column" : 70, "size" : 1},
    "NORMAL" : {"line" : 21, "column" : 70, "size" : 1},
    "TAQUICARDIA" : {"line" : 22, "column" : 70, "size" : 1}
}

linha_mensagem = 29

def limpar_tela():
    for campo, info in campos_historico.items:
        user_functions.limpar_linha(info["line"], info["column"], info["size"])

def iniciar():
    user_functions.limpar_tela()
    user_functions.desenhar_tela(layout_historico)
    user_functions.posicionarCursor(linha_mensagem, 98)
    print(constantes.OCULTAR_CURSOR)
    opcao = msvcrt.getch().decode("utf-8").upper()
    print(constantes.MOSTRAR_CURSOR)
    return opcao

def setar_tipo_temperatura(tipo_temperatura: TiposTemperatura=TiposTemperatura.NORMAL):
    linha = 19
    if tipo_temperatura == TiposTemperatura.HOPOTERMIA:
        linha = 18
    elif tipo_temperatura == TiposTemperatura.FEBRE_LEVE:
        linha = 20
    elif tipo_temperatura == TiposTemperatura.FEBRE_ALTA:
        linha = 21
    posicionarCursor(linha, 6)
    print("X")

def setar_tipo_pressao(tipo_pressao_arterial: TiposPressaoArterial=TiposPressaoArterial.NORMAL):
    linha = 19
    if tipo_pressao_arterial == TiposPressaoArterial.BAIXA:
        linha = 18
    elif tipo_pressao_arterial == TiposPressaoArterial.ALTA:
        linha = 20
    posicionarCursor(linha, 38)
    print("X")

def setar_tipo_frequencia(tipo_frequencia_cardiaca: TiposFrequenciaCardiaca=TiposFrequenciaCardiaca.NORMAL):    
    linha = 19
    if tipo_frequencia_cardiaca == TiposFrequenciaCardiaca.BRAQUICARDIA:
        linha = 18
    elif tipo_frequencia_cardiaca == TiposFrequenciaCardiaca.TARQUICARDIA:
        linha = 20
    posicionarCursor(linha, 70)
    print("X")

def setar_tipo_atendimento(tipo_atendimento: TiposAtendimento=TiposAtendimento.SEM_PREVISAO):
    coluna = 43
    if tipo_atendimento == TiposAtendimento.NORMAL:
        coluna = 60
    elif tipo_atendimento == TiposAtendimento.GRAVE:
        coluna = 71
    elif tipo_atendimento == TiposAtendimento.URGENTE:
        coluna = 81
    posicionarCursor(25, coluna)
    print("X")

def preencher_tela(historico: Historico):
    posicionarCursor(campos_historico["id"]["line"], campos_historico["id"]["column"])
    print(f"{str(historico.id).rjust(14, " ")}")
    posicionarCursor(campos_historico["data_exame"]["line"], campos_historico["data_exame"]["column"])
    print(formatar_data_hora(historico.data_exame))
    posicionarCursor(campos_historico["num_cpf"]["line"], campos_historico["num_cpf"]["column"])
    print(formatar_cpf(historico.num_cpf))
    paciente = basedados.lista_pacientes.get(str(historico.num_cpf))
    if paciente:
        posicionarCursor(campos_historico["nome_paciente"]["line"], campos_historico["nome_paciente"]["column"])
        print(paciente.nome_completo)
        posicionarCursor(campos_historico["data_nasc"]["line"], campos_historico["data_nasc"]["column"])
        print(formatar_data(paciente.data_nasc))
        idade = Paciente.calcular_idade(paciente.data_nasc)
        posicionarCursor(campos_historico["idade"]["line"], campos_historico["idade"]["column"])
        print(f"{str(idade).rjust(3, " ")}")
        posicionarCursor(campos_historico["nome_paciente"]["line"], campos_historico["nome_paciente"]["column"])
        print(paciente.nome_completo)
    posicionarCursor(campos_historico["temperatura"]["line"], campos_historico["temperatura"]["column"])
    print(f"{historico.temperatura:4.2f}".rjust(5, " "))
    posicionarCursor(campos_historico["pressao_arterial"]["line"], campos_historico["pressao_arterial"]["column"])
    print(f"{historico.pressao_arterial:4.2f}".rjust(5, " "))
    posicionarCursor(campos_historico["frequencia_cardiaca"]["line"], campos_historico["frequencia_cardiaca"]["column"])
    print(f"{historico.frequencia_cardiaca}".rjust(3, " "))
    setar_tipo_temperatura(historico.tipo_temperatura)
    setar_tipo_pressao(historico.tipo_pressao_arterial)
    setar_tipo_frequencia(historico.tipo_frequencia_cardiaca)
    setar_tipo_atendimento(historico.tipo_atendimento)

def digitar_id():
    info = campos_historico["id"]
    while True:
        user_functions.limpar_linha(linha_mensagem, 3, 95)
        user_functions.exibirMensagem(linha_mensagem, 3, "Digite o Número da Ficha de atendimento que deseja alterar")
        posicionarCursor(info["line"], info["column"])
        try:
            id = int(input())
            if id == 0:
                return False, None
            historico = basedados.historio_pacientes.get(str(id))
            if not historico:
                user_functions.exibirMensagem(linha_mensagem, 3, "Ficha de atendimento não cadastrada!")
                esperar_tecla()
                user_functions.limpar_linha(linha_mensagem, 3, 95)
                continue
            break
        except ValueError:
            user_functions.exibirMensagem(linha_mensagem, 3, "Número da Ficha de atendimento inválida!")
            esperar_tecla()
            user_functions.limpar_linha(linha_mensagem, 3, 95)
    user_functions.limpar_linha(linha_mensagem, 3, 95)
    return historico

def digitar_cpf():
    info = campos_historico["num_cpf"]
    while True:
        user_functions.limpar_linha(linha_mensagem, 3, 95)
        user_functions.exibirMensagem(linha_mensagem, 3, "Digite o CPF ou 99999999999 para sair")
        posicionarCursor(info["line"], info["column"])
        try:
            num_cpf = int(input())
            if num_cpf == 99999999999:
                break
            if not Paciente.validar_cpf(num_cpf):
                continue
            posicionarCursor(info["line"], info["column"])
            paciente = basedados.lista_pacientes.get(str(num_cpf))
            if not paciente:
                user_functions.exibirMensagem(linha_mensagem, 3, "Paciente não cadastrado")
                esperar_tecla()
                user_functions.limpar_linha(info["line"], info["column"], info["size"])
                continue
            print(formatar_cpf(num_cpf))
            posicionarCursor(campos_historico["data_nasc"]["line"], campos_historico["data_nasc"]["column"])
            print(formatar_data(paciente.data_nasc))
            idade = Paciente.calcular_idade(paciente.data_nasc)
            posicionarCursor(campos_historico["idade"]["line"], campos_historico["idade"]["column"])
            print(f"{str(idade).rjust(3, " ")}")
            posicionarCursor(campos_historico["nome_paciente"]["line"], campos_historico["nome_paciente"]["column"])
            print(paciente.nome_completo)
            break
        except ValueError:
            user_functions.exibirMensagem(linha_mensagem, 3, "Digite apenas os números do CPF")
            esperar_tecla()
            user_functions.limpar_linha(info["line"], info["column"], info["size"])

    user_functions.limpar_linha(linha_mensagem, 3, 95)
    return num_cpf, paciente

def digitar_temperatura():
    info = campos_historico["temperatura"]
    while True:
        user_functions.limpar_linha(linha_mensagem, 3, 95)
        user_functions.exibirMensagem(linha_mensagem, 3, "Digite a temperatura aferida")
        posicionarCursor(info["line"], info["column"])
        try:
            temperatura = float(input().replace(",", "."))
            tipo_temperatura = Historico.get_tipo_temperatura(temperatura)
            break
        except ValueError:
            user_functions.exibirMensagem(linha_mensagem, 3, "Valor da temperatura inválido!")
            esperar_tecla()
            user_functions.limpar_linha(info["line"], info["column"], info["size"])
    user_functions.limpar_linha(linha_mensagem, 3, 95)
    setar_tipo_temperatura(tipo_temperatura)
    return temperatura, tipo_temperatura

def digitar_pressao_arterial():
    info = campos_historico["pressao_arterial"]
    while True:
        user_functions.limpar_linha(linha_mensagem, 3, 95)
        user_functions.exibirMensagem(linha_mensagem, 3, "Digite a pressão arterial aferida")
        posicionarCursor(info["line"], info["column"])
        try:
            pressao_arterial = float(input().replace(",", "."))
            tipo_pressao_arterial = Historico.get_tipo_pressao_arterial(pressao_arterial)
            break
        except ValueError:
            user_functions.exibirMensagem(linha_mensagem, 3, "Valor da pressão arterial inválido!")
            esperar_tecla()
            user_functions.limpar_linha(info["line"], info["column"], info["size"])
            
    user_functions.limpar_linha(linha_mensagem, 3, 95)
    setar_tipo_pressao(tipo_pressao_arterial)
    return pressao_arterial, tipo_pressao_arterial

def digitar_frequencia_cardiaca():
    info = campos_historico["frequencia_cardiaca"]
    while True:
        user_functions.limpar_linha(linha_mensagem, 3, 95)
        user_functions.exibirMensagem(linha_mensagem, 3, "Digite a frequência cardíaca")
        posicionarCursor(info["line"], info["column"])
        try:
            frequencia_cardiaca = int(input())
            tipo_frequencia_cardiaca = Historico.get_tipo_frequencia_cardiaca(frequencia_cardiaca)
            break
        except ValueError:
            user_functions.exibirMensagem(linha_mensagem, 3, "Valor da frequência cardíaca inválido!")
            esperar_tecla()
            user_functions.limpar_linha(info["line"], info["column"], info["size"])
    user_functions.limpar_linha(linha_mensagem, 3, 95)
    setar_tipo_frequencia(tipo_frequencia_cardiaca)
    return frequencia_cardiaca, tipo_frequencia_cardiaca

def processar_digitacao(idAtendimento: int):
    num_cpf, paciente = digitar_cpf()
    if not paciente:
        return None
    temperatura, tipo_temperatura  = digitar_temperatura()
    pressao_arterial, tipo_pressao = digitar_pressao_arterial()
    frequencia_cardiaca, tipo_frequencia = digitar_frequencia_cardiaca()
    tipo_atendimento = Historico.get_tipo_atendimento(tipo_temperatura, tipo_pressao, tipo_frequencia);
    setar_tipo_atendimento(tipo_atendimento)
    posicionarCursor(27, 3)
    confirma = input("Confima os dados (S/N): ").upper()
    if confirma == "S":
        basedados.historio_pacientes[idAtendimento] = Historico(idAtendimento, datetime.now(), num_cpf, temperatura, tipo_temperatura,
                                                                pressao_arterial, tipo_pressao, frequencia_cardiaca, tipo_frequencia,
                                                                tipo_atendimento)
    user_functions.limpar_linha(27, 3, 95)

def novo_historico():
    if basedados.historio_pacientes:
        ultimoId = max(basedados.historio_pacientes.keys())
        proximoId = ultimoId + 1
    else:
        proximoId = 1
    processar_digitacao(proximoId)

def alterar_historico():
    historico = digitar_id()
    if not historico:
        return
    preencher_tela(historico)
    esperar_tecla()

def listar_historicos():
    user_functions.limpar_tela()
    user_functions.limpar_linha(29, 2, 97)
    user_functions.desenhar_tela(layout_rel_historicos, 8, 25)
    if not basedados.historio_pacientes:
        user_functions.exibirMensagem(29, 3, "Nenhum Histórico para ser exibido!")
        esperar_tecla()
        return
    else:
        linha = 7
        for id, historico in sorted(basedados.historio_pacientes.items(), key=lambda item: item[1].data_exame):
            linha += 1
            posicionarCursor(linha, 3)
            temp = f"{historico.temperatura:4.2f}".rjust(5, " ") 
            pressao = f'{historico.pressao_arterial:4.2f}'.rjust(5, " ")
            print(formatar_data_hora(historico.data_exame), Historico.get_nome_paciente(historico.num_cpf).ljust(39, " "), 
                  temp, pressao, str(historico.frequencia_cardiaca).rjust(3, " "), historico.tipo_atendimento.name, sep=" ║ ", end="")

    user_functions.exibirMensagem(29, 3, "Pressione qualquer tecla para continuar: ")
    esperar_tecla()
    
