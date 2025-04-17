import msvcrt
from datetime import datetime
from views.layout_telas import layout_paciente
from views.layout_telas import layout_rel_pacientes
from utils import user_functions, constantes
from utils.user_functions import formatar_cpf, formatar_cep, formatar_data, esperar_tecla
from models.tiposenum import TiposOperacao as tipo_operacao
from models.paciente import Paciente
from database import basedados

campos_paciente = {
    "num_cpf"  : { "line" :  7, "column" : 14, "size": 14 },
    "data_nasc": { "line" :  7, "column" : 74, "size": 10 },
    "idade"    : { "line" :  7, "column" : 94, "size":  3 },
    "nome"     : { "line" :  8, "column" : 14, "size": 83 },
    "endereco" : { "line" :  9, "column" : 14, "size": 62 },
    "numero"   : { "line" :  9, "column" : 87, "size": 10 },
    "compl"    : { "line" : 10, "column" : 14, "size": 28 },
    "bairro"   : { "line" : 10, "column" : 53, "size": 44 },
    "cep"      : { "line" : 11, "column" : 14, "size": 10 },
    "cidade"   : { "line" : 11, "column" : 37, "size": 51 },
    "uf"       : { "line" : 11, "column" : 95, "size":  2 },
    "telefone" : { "line" : 12, "column" : 14, "size": 13 }
}

linha_padrao_mensagem = 29
status_cad = tipo_operacao.CONSULTA

def limpa_tela():
    global campos_paciente
    #for chave, campos in campos_paciente.items():
    for campos in campos_paciente.items():
        user_functions.limpar_linha(campos[0], campos[1], campos[2])

def digitar_cpf():
    info = campos_paciente["num_cpf"]
    while True:
        user_functions.limpar_linha(linha_padrao_mensagem, 3, 95)
        user_functions.exibirMensagem(linha_padrao_mensagem, 3, "Digite o CPF ou 99999999999 para sair")
        user_functions.limpar_linha(info["line"], info["column"], info["size"])
        user_functions.posicionarCursor(info["line"], info["column"])
        try:
            num_cpf = int(input())
            if num_cpf == 99999999999:
                break
            if not Paciente.validar_cpf(num_cpf):
                continue
            user_functions.posicionarCursor(info["line"], info["column"])
            print(formatar_cpf(num_cpf))
            break
        except ValueError:
            user_functions.exibirMensagem(linha_padrao_mensagem, 3, "Digite apenas os números do CPF")
            esperar_tecla()
    user_functions.limpar_linha(linha_padrao_mensagem, 3, 95)
    return num_cpf

def digitar_data_nasc():
    global status_cad
    localizacao = campos_paciente["data_nasc"]
    localizacao_idade = campos_paciente["idade"]
    while True:
        user_functions.limpar_linha(linha_padrao_mensagem, 2, 97)
        user_functions.limpar_linha(localizacao["line"], localizacao["column"], localizacao["size"])
        user_functions.exibirMensagem(linha_padrao_mensagem, 3, "Digite a data de nascimento")
        user_functions.posicionarCursor(localizacao["line"], localizacao["column"])
        try:
            str_data = input()
            if str_data == "":
                data_nasc = datetime.min.date()
                break
            fl_data_ok, data_nasc, mensagem = user_functions.validar_data(str_data)
            
            if not fl_data_ok:
                user_functions.limpar_linha(linha_padrao_mensagem, 2, 97)
                user_functions.exibirMensagem(linha_padrao_mensagem, 3, mensagem)
                esperar_tecla()
                continue
            idade = Paciente.calcular_idade(data_nasc)
            user_functions.posicionarCursor(localizacao_idade["line"], localizacao_idade["column"])
            print(str(idade).rjust(3, " "))
            break
        except Exception as ex:
            user_functions.limpar_linha(linha_padrao_mensagem, 2, 97)
            user_functions.exibirMensagem(linha_padrao_mensagem, 3, f"Data Inválida: {ex}")
            esperar_tecla()
    user_functions.limpar_linha(linha_padrao_mensagem, 3, 95)
    user_functions.posicionarCursor(localizacao["line"], localizacao["column"])
    print(formatar_data(data_nasc))
    return data_nasc

def digitar_nome():
    localizacao = campos_paciente["nome"]
    while True:
        user_functions.limpar_linha(linha_padrao_mensagem, 3, 95)
        user_functions.limpar_linha(localizacao["line"], localizacao["column"], localizacao["size"])
        user_functions.exibirMensagem(linha_padrao_mensagem, 3, "Digite o nome completo do Paciente.")
        user_functions.posicionarCursor(localizacao["line"], localizacao["column"])
        nome = input().title()
        fl_ok, mensagem = Paciente.validar_nome(nome, "do paciente")
        if not fl_ok:
            user_functions.exibirMensagem(linha_padrao_mensagem, 3, mensagem)
            esperar_tecla()
            user_functions.limpar_linha(linha_padrao_mensagem, 3, 95)
            continue
        break
    user_functions.limpar_linha(linha_padrao_mensagem, 3, 95)
    user_functions.posicionarCursor(localizacao["line"], localizacao["column"])
    print(nome)
    return nome

def digitar_endereco():
    localizacao = campos_paciente["endereco"]
    user_functions.limpar_linha(linha_padrao_mensagem, 3, 95)
    user_functions.limpar_linha(localizacao["line"], localizacao["column"], localizacao["size"])
    user_functions.exibirMensagem(linha_padrao_mensagem, 3, "Digite o endereço do Paciente.")
    user_functions.posicionarCursor(localizacao["line"], localizacao["column"])
    endereco = input().title()
    user_functions.limpar_linha(linha_padrao_mensagem, 3, 95)
    user_functions.posicionarCursor(localizacao["line"], localizacao["column"])
    print(endereco)
    return endereco

def digitar_numero():
    localizacao = campos_paciente["numero"]
    user_functions.limpar_linha(linha_padrao_mensagem, 3, 95)
    user_functions.limpar_linha(localizacao["line"], localizacao["column"], localizacao["size"])
    user_functions.exibirMensagem(linha_padrao_mensagem, 3, "Digite o número endereço do Paciente.")
    user_functions.posicionarCursor(localizacao["line"], localizacao["column"])
    numero = input().title()
    user_functions.limpar_linha(linha_padrao_mensagem, 3, 95)
    user_functions.posicionarCursor(localizacao["line"], localizacao["column"])
    print(numero)
    return numero

def digitar_complemento():
    localizacao = campos_paciente["compl"]
    user_functions.limpar_linha(linha_padrao_mensagem, 3, 95)
    user_functions.limpar_linha(localizacao["line"], localizacao["column"], localizacao["size"])
    user_functions.exibirMensagem(linha_padrao_mensagem, 3, "Digite o complemento endereço do Paciente.")
    user_functions.posicionarCursor(localizacao["line"], localizacao["column"])
    complemento = input().title()
    user_functions.limpar_linha(linha_padrao_mensagem, 3, 95)
    user_functions.posicionarCursor(localizacao["line"], localizacao["column"])
    print(complemento)
    return complemento

def digitar_bairro():
    localizacao = campos_paciente["bairro"]
    user_functions.limpar_linha(linha_padrao_mensagem, 3, 95)
    user_functions.limpar_linha(localizacao["line"], localizacao["column"], localizacao["size"])
    user_functions.exibirMensagem(linha_padrao_mensagem, 3, "Digite o bairro do endereço do Paciente.")
    user_functions.posicionarCursor(localizacao["line"], localizacao["column"])
    bairro = input().title()
    user_functions.limpar_linha(linha_padrao_mensagem, 3, 95)
    user_functions.posicionarCursor(localizacao["line"], localizacao["column"])
    print(bairro)
    return bairro

def digitar_cep():
    localizacao = campos_paciente["cep"]
    while True:
        try:
            user_functions.limpar_linha(linha_padrao_mensagem, 3, 95)
            user_functions.limpar_linha(localizacao["line"], localizacao["column"], localizacao["size"])
            user_functions.exibirMensagem(linha_padrao_mensagem, 3, "Digite o cep do endereço do Paciente.")
            user_functions.posicionarCursor(localizacao["line"], localizacao["column"])
            cep = int(input())
            break
        except:
            user_functions.exibirMensagem(linha_padrao_mensagem, 3, "CEP inválido! Digite apenas os números")
            esperar_tecla()
            user_functions.limpar_linha(linha_padrao_mensagem, 3, 95)
            continue
    user_functions.limpar_linha(linha_padrao_mensagem, 3, 95)
    user_functions.posicionarCursor(localizacao["line"], localizacao["column"])
    print(formatar_cep(cep))
    return cep

def digitar_cidade():
    localizacao = campos_paciente["cidade"]
    while True:
        user_functions.limpar_linha(linha_padrao_mensagem, 3, 95)
        user_functions.limpar_linha(linha_padrao_mensagem, 3, 95)
        user_functions.limpar_linha(localizacao["line"], localizacao["column"], localizacao["size"])
        user_functions.exibirMensagem(linha_padrao_mensagem, 3, "Digite o cidade do Paciente.")
        user_functions.posicionarCursor(localizacao["line"], localizacao["column"])
        cidade = input().title()
        fl_ok, mensagem = Paciente.validar_nome(cidade, "da cidade")
        if not fl_ok:
            user_functions.exibirMensagem(linha_padrao_mensagem, 3, mensagem)
            esperar_tecla()
            user_functions.limpar_linha(linha_padrao_mensagem, 3, 95)
            continue
        break
    user_functions.limpar_linha(linha_padrao_mensagem, 3, 95)
    user_functions.posicionarCursor(localizacao["line"], localizacao["column"])
    print(cidade)
    return cidade

def digitar_uf():
    localizacao = campos_paciente["uf"]
    while True:
        user_functions.limpar_linha(linha_padrao_mensagem, 3, 95)
        user_functions.limpar_linha(localizacao["line"], localizacao["column"], localizacao["size"])
        user_functions.exibirMensagem(linha_padrao_mensagem, 3, "Informe o Estado do qual a Cidade pertence")
        user_functions.posicionarCursor(localizacao["line"], localizacao["column"])
        uf = input().upper()
        fl_ok, mensagem = user_functions.validar_estado(uf)
        if not fl_ok:
            user_functions.exibirMensagem(linha_padrao_mensagem, 3, mensagem)
            esperar_tecla()
            user_functions.limpar_linha(linha_padrao_mensagem, 3, 95)
            continue
        break
    user_functions.posicionarCursor(localizacao["line"], localizacao["column"])
    print(uf)
    return uf

def digitar_telefone():
    localizacao = campos_paciente["telefone"]
    user_functions.limpar_linha(linha_padrao_mensagem, 3, 95)
    user_functions.limpar_linha(localizacao["line"], localizacao["column"], localizacao["size"])
    user_functions.exibirMensagem(linha_padrao_mensagem, 3, "Digite o número do telefone com DDD do Paciente.")
    user_functions.posicionarCursor(localizacao["line"], localizacao["column"])
    telefone = input()
    user_functions.limpar_linha(linha_padrao_mensagem, 3, 95)
    return telefone

def preencher_dados(paciente: Paciente):
    user_functions.posicionarCursor(campos_paciente["num_cpf"]["line"], campos_paciente["num_cpf"]["column"])
    print(formatar_cpf(paciente.num_cpf))
    user_functions.posicionarCursor(campos_paciente["data_nasc"]["line"], campos_paciente["data_nasc"]["column"])
    print(formatar_data(paciente.data_nasc))
    idade = Paciente.calcular_idade(paciente.data_nasc)
    user_functions.posicionarCursor(campos_paciente["idade"]["line"], campos_paciente["idade"]["column"])
    print(str(idade).rjust(3, " "))
    user_functions.posicionarCursor(campos_paciente["nome"]["line"], campos_paciente["nome"]["column"])
    print(paciente.nome_completo)
    user_functions.posicionarCursor(campos_paciente["endereco"]["line"], campos_paciente["endereco"]["column"])
    print(paciente.endereco)
    user_functions.posicionarCursor(campos_paciente["numero"]["line"], campos_paciente["numero"]["column"])
    print(paciente.numero)
    user_functions.posicionarCursor(campos_paciente["compl"]["line"], campos_paciente["compl"]["column"])
    print(paciente.complemento)
    user_functions.posicionarCursor(campos_paciente["bairro"]["line"], campos_paciente["bairro"]["column"])
    print(paciente.bairro)
    user_functions.posicionarCursor(campos_paciente["cep"]["line"], campos_paciente["cep"]["column"])
    print(formatar_cep(paciente.cep))
    user_functions.posicionarCursor(campos_paciente["cidade"]["line"], campos_paciente["cidade"]["column"])
    print(paciente.cidade)
    user_functions.posicionarCursor(campos_paciente["uf"]["line"], campos_paciente["uf"]["column"])
    print(paciente.uf)
    user_functions.posicionarCursor(campos_paciente["telefone"]["line"], campos_paciente["telefone"]["column"])
    print(paciente.telefone)

def processar_digitacao(num_cpf: int):
    global status_cad
    data_nasc = digitar_data_nasc()
    nome = digitar_nome()
    endereco = digitar_endereco()
    numero = digitar_numero()
    compl = digitar_complemento()
    bairro = digitar_bairro()
    cep = digitar_cep()
    cidade = digitar_cidade()
    uf = digitar_uf()
    telefone = digitar_telefone()
    user_functions.exibirMensagem(16, 3, "Confirmar os dados? (S/N) [ ]")
    user_functions.posicionarCursor(16, 30)
    if input().upper() == "S":
       basedados.lista_pacientes[num_cpf] = Paciente(num_cpf, nome, endereco, numero, compl, bairro, cep, cidade, uf, data_nasc, telefone)
    user_functions.limpar_linha(16, 2, 97)
    status_cad = tipo_operacao.CONSULTA

def iniciar():
    user_functions.limpar_tela()
    user_functions.desenhar_tela(layout_paciente)
    user_functions.posicionarCursor(30, 98)
    print(constantes.OCULTAR_CURSOR)
    opcao = msvcrt.getch().decode("utf-8").upper()
    print(constantes.MOSTRAR_CURSOR)
    return opcao

def novo_paciente():
    global status_cad
    num_cpf = digitar_cpf()
    if num_cpf == 99999999999:
        return None
    paciente = basedados.lista_pacientes.get(str(num_cpf))
    if paciente:
        user_functions.exibirMensagem(linha_padrao_mensagem, 3, "CPF já cadastrado!")
        esperar_tecla()
        return None
    status_cad = tipo_operacao.INCLUSAO
    processar_digitacao(num_cpf)

def alterar_paciente():
    global status_cad
    num_cpf = digitar_cpf()
    if num_cpf == 99999999999:
        return None
    paciente = basedados.lista_pacientes.get(str(num_cpf))
    if not paciente:
        user_functions.exibirMensagem(linha_padrao_mensagem, 3, "CPF não cadastrado!")
        esperar_tecla()
        return None
    preencher_dados(paciente)
    status_cad = tipo_operacao.ALTERACAO
    user_functions.esperar_tecla();
    processar_digitacao(num_cpf)

def excluir_paciente():
    global status_cad
    num_cpf = digitar_cpf()
    if num_cpf == 99999999999:
        return None
    paciente = basedados.lista_pacientes.get(str(num_cpf))
    if not paciente:
        user_functions.exibirMensagem(linha_padrao_mensagem, 3, "CPF não cadastrado!")
        esperar_tecla()
        return None
    preencher_dados(paciente)
    status_cad = tipo_operacao.EXCLUSAO

def listar_pacientes():
    user_functions.limpar_tela()
    user_functions.limpar_linha(29, 2, 97)
    user_functions.desenhar_tela(layout_rel_pacientes, 8, 27)
    if not basedados.lista_pacientes:
        user_functions.exibirMensagem("Nenhum paciente para ser exibido!")
        esperar_tecla()
        return
    else:
        linha = 7
        for cpf, paciente in sorted(basedados.lista_pacientes.items(), key=lambda item: item[1].nome_completo):
            linha += 1
            user_functions.posicionarCursor(linha, 3)
            print(formatar_cpf(paciente.num_cpf), paciente.nome_completo.ljust(62, " "), paciente.telefone.ljust(13, " "), sep=" ║ ", end="")
    user_functions.exibirMensagem(29, 3, "Pressione qualquer tecla para continuar: ")
    esperar_tecla()

