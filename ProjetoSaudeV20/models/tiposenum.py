from enum import Enum

mascara_data_br = "%d/%m/%Y"
estados = [
    "AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA",
    "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN",
    "RO", "RR", "RS", "SC", "SE", "SP", "TO"
]

class TiposTemperatura(Enum):
    HOPOTERMIA = 0
    NORMAL = 1
    FEBRE_LEVE = 2
    FEBRE_ALTA = 3

class TiposPressaoArterial(Enum):
    BAIXA = 0
    NORMAL = 1
    ALTA = 2

class TiposFrequenciaCardiaca(Enum):
    BRAQUICARDIA = 0
    NORMAL = 1
    TARQUICARDIA = 2

class TiposAtendimento(Enum):
    SEM_PREVISAO = 0
    NORMAL = 1
    GRAVE = 2
    URGENTE = 3

class TiposOperacao(Enum):
    CONSULTA = 0
    INCLUSAO = 1
    ALTERACAO = 2
    EXCLUSAO = 3