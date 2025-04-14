from datetime import datetime
from tiposenum import TiposTemperatura
from tiposenum import TiposPressaoArterial
from tiposenum import TiposFrequenciaCardiaca
from tiposenum import TiposAtendimento

class Historico():
    def __init__(self, id: int, data_hora: datetime, cpf_paciente: int, temperatura: float, tipo_temperatura: TiposTemperatura,
                 pressao_arterial: float, tipo_pressao: TiposPressaoArterial, 
                 frequencia_cardiaca: float, tipo_frequencia_cardio: TiposFrequenciaCardiaca,
                 tipo_atendimento: TiposAtendimento, observacoes: str=""):
        self.id = id
        self.data_hora = data_hora
        self.cpf_paciente = cpf_paciente
        self.temperatura = temperatura
        self.temperatura = tipo_temperatura
        self.pressao_arterial = pressao_arterial
        self.tipo_pressao = tipo_pressao
        self.frequencia_cardiaca = frequencia_cardiaca
        self.tipo_frequencia_cardio = tipo_frequencia_cardio
        self.tipo_atendimento = tipo_atendimento
        self.observacoes = observacoes
        