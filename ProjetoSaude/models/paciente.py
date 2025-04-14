from datetime import date

class Paciente():
    def __init__(self, num_cpf: int, nome_completo: str, data_nasc: date, telefone: str, cidade: str, uf: str, cep: int=0,
                 endereco: str="", numero: str="", complemento: str="", bairro: str=""):
        self.num_cpf = num_cpf
        self.nome_completo = nome_completo
        self.data_nasc = data_nasc
        self.telefone = telefone
        self.cidade = cidade
        self.uf = uf
        self.cep = cep
        self.endereco = endereco
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro

    def get_idade(self):
        idade = date.today().year - self.data_nasc.year
        
        if ((date.today().month < self.data_nasc.month) or (date.today().month == self.data_nasc.month and date.today().day) < self.data_nasc.day))
            idade -= 1
        
        return idade
    