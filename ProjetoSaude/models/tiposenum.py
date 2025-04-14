from enum import Enum, auto

class TiposTemperatura(Enum):
    HIPOTERMIA = auto()
    NORMAL = auto()
    FEBRE_LEVE = auto()
    FEBRE_ALTA = auto()

class TiposPressaoArterial(Enum):
    BAIXA = auto()
    NORMAL = auto()
    ALTA = auto()

class TiposFrequenciaCardiaca(Enum):
    BRAQUICARDA = auto()
    NORMAL = auto()
    TAQUICARDIA = auto()

class TiposAtendimento(Enum):
    SEM_PREVISAO = auto()
    NORMAL = auto()
    GRAVE = auto()
    URGENTE = auto()

class TiposOperacao(Enum):
    INCLUSAO = 0
    ALTERACAO = 1
    EXCLUSAO = 2
    CONSULTA = 3