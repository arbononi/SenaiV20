from utils import user_functions
from models.paciente import Paciente
from views.layout_telas import layout_paciente, layout_rel_pacientes
from views.paciente_view import iniciar, novo_paciente, alterar_paciente, excluir_paciente, listar_pacientes
from models.tiposenum import TiposOperacao as status_cad

opcoes_disponiveis = [ "N", "A", "E", "C", "L", "R" ]

class PacienteController:
    def __init__(self):
        pass
    
    def iniciar(self):
        while True:
            opcao = iniciar()
            if opcao not in opcoes_disponiveis:
                user_functions.limpar_linha(29, 2, 97)
                user_functions.posicionarCursor(29, 3)
                input(f"Opção inválida! Escolha uma entre essas: {opcoes_disponiveis}!")
                user_functions.limpar_linha(29, 2, 97)
                user_functions.posicionarCursor(layout_paciente[8]["line"], layout_paciente[8]["column"])
                print(layout_paciente[8]["value"])
                continue
            if opcao == "R":
                user_functions.posicionarCursor(layout_paciente[1]["line"], 1)
                print("║")
                user_functions.posicionarCursor(layout_paciente[1]["line"], 99)
                print("║")
                break
            if opcao == "N":
                novo_paciente()
            elif opcao == "A":
                alterar_paciente()
            elif opcao == "E":
                excluir_paciente()
            elif opcao == "L":
                listar_pacientes()
                user_functions.posicionarCursor(layout_rel_pacientes[3]["line"], 1)
                print("║")
                user_functions.posicionarCursor(layout_rel_pacientes[5]["line"], 2)
                print("═" * 97)
                user_functions.posicionarCursor(layout_rel_pacientes[3]["line"], 99)
                print("║")

