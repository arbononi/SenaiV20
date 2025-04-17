from datetime import datetime, date
from utils.user_functions import validar_cpf
from utils.user_functions import exibirMensagem

class Paciente:
    def __init__(self, num_cpf: int, nome_completo: str, endereco: str, numero: str, complemento: str,
                 bairro: str, cep: int, cidade: str, uf: str, data_nasc: date, telefone: str):
        self.num_cpf = num_cpf
        self.nome_completo = nome_completo
        self.endereco = endereco
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cep = cep
        self.cidade = cidade
        self.uf = uf.upper()
        self.data_nasc = data_nasc
        self.telefone = telefone
    
    def validar_cpf(num_cpf: int):
        cpf_ok, mensagem = validar_cpf(num_cpf)
        if not cpf_ok:
            exibirMensagem(29, 3, mensagem)
            input()
        return cpf_ok
            
    def validar_nome(nome: str, campo: str):
        if nome.strip() == "":
            return False, f"Nome {campo} não pode ficar em branco"
        return True, None
    
    def validar_cidade(cidade: str):
        if cidade.strip() == "":
            return False, "Nome da Cidade não pode ficar em branco"
        return True, None
    
    def calcular_idade(dataNasc : date):
        idade = date.today().year - dataNasc.year
        if (date.today().month < dataNasc.month) or (date.today().month == dataNasc.month and date.today().day < dataNasc.day):
            idade -= 1
        return idade
