from utils import user_functions
from models.historico import Historico
from views.layout_telas import layout_historico, layout_rel_historicos
from views.historico_view import iniciar, novo_historico, alterar_historico, listar_historicos
from models.tiposenum import TiposOperacao as status_cad

opcoes_disponiveis = [ "N", "A", "S", "E", "C", "L", "R" ]

class HistoricoController:
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
                user_functions.posicionarCursor(layout_historico[18]["line"], layout_historico[18]["column"])
                print(layout_historico[18]["value"])
                continue
            if opcao == "N":
               novo_historico()
            elif opcao == "A":
                alterar_historico()
            elif opcao == "R":
                user_functions.posicionarCursor(layout_historico[1]["line"], 1)
                print("║")
                user_functions.posicionarCursor(layout_historico[1]["line"], 99)
                print("║")
                user_functions.posicionarCursor(layout_historico[5]["line"], 1)
                print("║")
                user_functions.posicionarCursor(layout_historico[5]["line"], 99)
                print("║")
                user_functions.posicionarCursor(layout_historico[7]["line"], 1)
                print("║")
                user_functions.posicionarCursor(layout_historico[7]["line"], 99)
                print("║")
                break
            elif opcao == "L":
                listar_historicos()
                user_functions.posicionarCursor(layout_rel_historicos[1]["line"], 1)
                print("║")
                user_functions.posicionarCursor(layout_rel_historicos[3]["line"], 1)
                print("═" * 97)
                user_functions.posicionarCursor(layout_rel_historicos[5]["line"], 1)
                print("║")
                user_functions.posicionarCursor(layout_rel_historicos[5]["line"], 99)
                print("║")
            
