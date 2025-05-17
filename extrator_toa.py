# extrator_toa.py

import time
import random

def extrair_planilha_toa(login, senha, oma):
    """
    Simula a extração da planilha do TOA.
    Essa versão é temporária, apenas para testar o painel Streamlit.
    """
    time.sleep(2)  # Simula tempo de carregamento

    # Simula aleatoriamente sucesso ou erro
    if random.choice([True, False]):
        return True, "Arquivo baixado com sucesso (simulado)."
    else:
        return False, "Erro simulado: Falha ao autenticar no TOA."
