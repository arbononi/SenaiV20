import locale
import csv
from  models import tiposenum
from os import system as limp
from pathlib import Path
from time import sleep
from datetime import date, datetime
from views.layout_telas import layout_tela_principal
from utils import user_functions
from controllers.paciente_controller import PacienteController
from controllers.historico_controller import HistoricoController
from database import basedados
from models.paciente import Paciente
from models.historico import Historico

opcoes_menu_principal = [
    { "line" :  5, "column" : 3, "value" : "1 - Cadastro de Pacientes" },
    { "line" :  6, "column" : 3, "value" : "2 - Atendimento a Paciente" },
    { "line" :  7, "column" : 3, "value" : "3 - Carregar Pacientes de Arquivo" },
    { "line" :  8, "column" : 3, "value" : "4 - Carregar Histórico de Arquivo" },
    { "line" : 26, "column" : 3, "value" : "9 - Encerrar Sistema" },
    { "line" : 29, "column" : 3, "value" : "Escolha a opção desejada: [ ]" }
]

locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')
limp("cls")
opcao = 0
opcao_limite = 4
linha_mensagem = 29
data_atual_str = user_functions.formatar_data(date.today()) 
pasta_projeto = Path().resolve()
caminho_arquivo_pacientes = pasta_projeto / "Lista_Pacientes.csv"
caminho_arquivo_historicos = pasta_projeto / "Lista_Historicos.csv"

def CarregarPacientesDoArquivo(leitura_inicial: bool=False):
    with open(caminho_arquivo_pacientes, newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=";")
        for linha in leitor:
            fl_ok, data, mensagem = user_functions.validar_data(linha["data_nasc"])
            if not fl_ok:
                data = datetime.min.date()
            
            basedados.lista_pacientes[linha["num_cpf"]] = Paciente(int(linha["num_cpf"]), linha["nome_completo"], 
                                                                   linha["endereco"], linha["numero"], linha["complemento"],
                                                                   linha["bairro"], int(linha["cep"]), linha["cidade"],
                                                                   linha["uf"], data, linha["telefone"])
    if not leitura_inicial:
        user_functions.posicionarCursor(linha_mensagem, 3)
        input("Dados importados com sucesso!!")

def CarregarHistoricosDoArquivo(leitura_inicial: bool=False):
    with open(caminho_arquivo_historicos, newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=";")
        for linha in leitor:
            #paciente = basedados.lista_pacientes.get(str(num_cpf))
            paciente = basedados.lista_pacientes.get(linha["num_cpf"])
            if not paciente:
                continue
            fl_ok, data_exame, mensagem = user_functions.validar_data_hora(linha["data_exame"])
            if not fl_ok:
                data_exame = datetime.now()
            tipo_temperatura = tiposenum.TiposTemperatura(int(linha["tipo_temperatura"]))
            tipo_pressao = tiposenum.TiposPressaoArterial(int(linha["tipo_pressao_arterial"]))
            tipo_frequencia = tiposenum.TiposFrequenciaCardiaca(int(linha["tipo_frequencia_cardiaca"]))
            tipo_atendimento = tiposenum.TiposAtendimento(int(linha["tipo_atendimento"]))

            basedados.historio_pacientes[linha["id"]] = Historico(int(linha["id"]), data_exame, int(linha["num_cpf"]),
                                                                  float(linha["temperatura"]), tipo_temperatura, 
                                                                  float(linha["pressao_arterial"]), tipo_pressao,
                                                                  int(linha["frequencia_cardiaca"]), tipo_frequencia,
                                                                  tipo_atendimento)
    if not leitura_inicial:
        user_functions.posicionarCursor(linha_mensagem, 3)
        input("Dados importados com sucesso!!")

user_functions.posicionarCursor(1, 1)
user_functions.desenhar_tela(layout_tela_principal)
user_functions.posicionarCursor(2, 84)
print(data_atual_str)

user_functions.desenhar_tela(opcoes_menu_principal)

if caminho_arquivo_pacientes.exists():
    CarregarPacientesDoArquivo(True)

if caminho_arquivo_historicos.exists() and basedados.lista_pacientes:
    CarregarHistoricosDoArquivo(True)

while opcao != 9:
    try:
        user_functions.posicionarCursor(linha_mensagem, 30)
        opcao = int(input())

        if ((opcao < 1 or opcao > opcao_limite) and opcao != 9):
            user_functions.exibirMensagem(linha_mensagem, 3, f"Opção inválida. Escolha entre 1 e {opcao_limite} ou 9.")
            user_functions.esperar_tecla()
            user_functions.limpar_linha(linha_mensagem, 3, 95)
            user_functions.posicionarCursor(linha_mensagem, 3)
            print(opcoes_menu_principal[opcao_limite + 1]["value"])
            continue

        if opcao == 9:
            break;

        if opcao == 1:
            app = PacienteController()
            app.iniciar()
        elif opcao == 2:
            app = HistoricoController()
            app.iniciar()
        elif opcao == 3:
            CarregarPacientesDoArquivo()
        elif opcao == 4:
            CarregarHistoricosDoArquivo()

        user_functions.limpar_tela()
        user_functions.limpar_linha(linha_mensagem, 3, 95)
        user_functions.desenhar_tela(opcoes_menu_principal)
        user_functions.posicionarCursor(linha_mensagem, 30)
        
    except ValueError:
        user_functions.exibirMensagem(linha_mensagem, 3, "Opção inválida! Apenas números são permitidos")
        user_functions.esperar_tecla()
        user_functions.limpar_linha(linha_mensagem, 3, 95)
        print(opcoes_menu_principal[opcao_limite + 1]["value"])


user_functions.exibirMensagem(linha_mensagem, 3, "Obrigado por usar nossos serviços. Volte sempre!!")
sleep(1)
limp("cls")
