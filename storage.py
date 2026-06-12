import json

from tarefa import Tarefa


ARQUIVO_TAREFAS = "tarefas.json"


def carregar_tarefas():

    try:
        with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []

    tarefas = []
    for item in dados:
        tarefa = Tarefa.criar_de_dicionario(item)
        tarefas.append(tarefa)

    return tarefas


def salvar_tarefas(tarefas):

    dados = []

    for tarefa in tarefas:
        dados.append(tarefa.transformar_em_dicionario())

    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)