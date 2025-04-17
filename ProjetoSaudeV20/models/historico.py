from datetime import datetime
from models.tiposenum import TiposTemperatura, TiposPressaoArterial, TiposFrequenciaCardiaca, TiposAtendimento
from database import basedados

class Historico:
    def __init__(self, id: int, data_exame: datetime, num_cpf: int, temperatura: float, tipo_temperatura : TiposTemperatura,
                 pressao_arterial: float, tipo_pressao_arterial: TiposPressaoArterial, 
                 frequencia_cardiaca: float, tipo_frequencia_cardiaca: TiposFrequenciaCardiaca, tipo_atendimento: TiposAtendimento):
        self.id = id
        self.data_exame = data_exame
        self.num_cpf = num_cpf
        self.temperatura = temperatura
        self.tipo_temperatura = tipo_temperatura
        self.pressao_arterial = pressao_arterial
        self.tipo_pressao_arterial = tipo_pressao_arterial
        self.frequencia_cardiaca = frequencia_cardiaca
        self.tipo_frequencia_cardiaca = tipo_frequencia_cardiaca
        self.tipo_atendimento = tipo_atendimento

    def get_nome_paciente(num_cpf: int):
        paciente = basedados.lista_pacientes.get(str(num_cpf))
        if paciente:
            return paciente.nome_completo
        return ""
        
    # Temperatura Corporal
    # - Hipotermia (Abaixo de 35° C)
    # - Normal (Entre 35° C e 37.5° C)
    # - Febre Leve (de 37.6°C A 39° C)
    # - Febre Alta (acima de 39° C)
    def get_tipo_temperatura(temperatura: float):
        if temperatura < 35:
            return TiposTemperatura.HOPOTERMIA
        elif temperatura > 37.5 and temperatura < 39:
            return TiposTemperatura.FEBRE_LEVE
        elif temperatura > 39:
            return TiposTemperatura.FEBRE_ALTA
        return TiposTemperatura.NORMAL
    
    # Pressão Arterial
    # - Baixa (Menor que 10)
    # - Normal (Entre 10.1 e 14)
    # - Alta  (Maior que 14)
    def get_tipo_pressao_arterial(pressao_arterial: float):
        if pressao_arterial <= 10:
            return TiposPressaoArterial.BAIXA
        elif pressao_arterial > 14:
            return TiposPressaoArterial.ALTA
        return TiposPressaoArterial.NORMAL

    # Frequência Cardíaca
    # Bradicardia (Abaixo de 60 BPM)
    # Normal (Entre 60 e 100 BPM)
    # Taquicardia (Acima de 100 BPM)
    def get_tipo_frequencia_cardiaca(frequencia: float):
        if frequencia < 60:
            return TiposFrequenciaCardiaca.BRAQUICARDIA
        elif frequencia > 100:
            return TiposFrequenciaCardiaca.TARQUICARDIA
        return TiposFrequenciaCardiaca.NORMAL
    
    # Classificação do atendimento

    # Atendimento normal
    # - Temperatura : Normal ou Febre Leve
    # - Pressão Arterial: Normal
    # - Batimentos  : Normal

    # Atendimento Grave
    # - Temperatura : Febre Alta
    # - Pressão Arterial: Alta
    # - Batimentos  : Taquicardia

    # Atendimento Urgente
    # - Temperatura : Hipotermia
    # - Pressão Arterial: Baixa
    # - Batimentos  : Braquicardia
    def get_tipo_atendimento(tipo_temperatura: TiposTemperatura, tipo_pressao: TiposPressaoArterial, tipo_frequencia: TiposFrequenciaCardiaca):
        if tipo_temperatura == TiposTemperatura.HOPOTERMIA and tipo_pressao == TiposPressaoArterial.BAIXA and tipo_frequencia == TiposFrequenciaCardiaca.BRAQUICARDIA:
            return TiposAtendimento.URGENTE
        elif tipo_temperatura == TiposTemperatura.FEBRE_ALTA and tipo_pressao == TiposPressaoArterial.ALTA and tipo_frequencia == TiposFrequenciaCardiaca.TARQUICARDIA:
            return TiposAtendimento.GRAVE
        elif (tipo_temperatura == TiposTemperatura.NORMAL or tipo_temperatura == TiposTemperatura.FEBRE_LEVE) and tipo_pressao == TiposPressaoArterial.NORMAL and tipo_frequencia == TiposFrequenciaCardiaca.NORMAL:
            return TiposAtendimento.NORMAL
        return TiposAtendimento.SEM_PREVISAO
    
    def get_tipo_atendimento(tipo_atendimento: int = 0):
        if (tipo_atendimento == 1):
            return TiposAtendimento.NORMAL
        elif tipo_atendimento == 2:
            return TiposAtendimento.GRAVE
        elif tipo_atendimento == 3:
            return TiposAtendimento.URGENTE
        
        return TiposAtendimento.SEM_PREVISAO
        
