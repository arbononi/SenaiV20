import sys

def limpar_linha(linha: int, coluna: int, tamanho: int):
    posicionarCursor(linha, coluna)
    print(" " * tamanho)
    posicionarCursor(linha, coluna)

def posicionarCursor(linha: int, coluna: int):
    sys.stdout.write(f"\033[{linha};{coluna}H")

def exibirMensagem(linha: int, coluna: int, mensagem: str, saltar_linha: str =" "):
    posicionarCursor(linha, coluna)
    print(mensagem, end=saltar_linha)

def limpar_tela(start: int, stop: int, column: int, size: int):
    for linha in range(start, stop):
        posicionarCursor(linha, column)
        print(" " * size, end="")

def desenhar_tela(linha_inicial: int, coluna: int, layout, indice_opcoes: int, linha_opcoes: int):
    indice = 1
    for texto in layout:
        if indice_opcoes > 0 and indice == indice_opcoes:
            linha_inicial = linha_opcoes
        posicionarCursor(linha_inicial, coluna)
        print(texto, end="")
        linha_inicial += 1
