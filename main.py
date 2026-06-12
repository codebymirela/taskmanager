from tarefa import Tarefa
from storage import carregar_tarefas, salvar_tarefas


def mostrar_menu():
    print("\n=== Gerenciador de Tarefas ===")
    print("1. Criar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Listar tarefas pendentes")
    print("6. Listar tarefas concluídas")
    print("7. Buscar tarefa")
    print("8. Sair")


def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\nSuas tarefas:")

    for indice, tarefa in enumerate(tarefas, start=1):
        status = "Concluída" if tarefa.concluida else "Pendente"

        print(
            f"{indice}. {tarefa.titulo} - {status} "
            f"- Prioridade: {tarefa.prioridade} "
            f"- Categoria: {tarefa.categoria}"
        )


def criar_tarefa(tarefas):
    titulo = input("Digite o título da tarefa: ").strip()

    if not titulo:
        print("O título da tarefa não pode ficar vazio.")
        return

    prioridade = input("Prioridade [baixa/média/alta]: ").strip().lower()

    if prioridade not in ["baixa", "média", "alta"]:
        prioridade = "média"

    categoria = input("Categoria da tarefa: ").strip().lower()

    if not categoria:
        categoria = "geral"

    tarefa = Tarefa(titulo, prioridade, categoria)

    tarefas.append(tarefa)
    salvar_tarefas(tarefas)

    print("Tarefa criada com sucesso.")


def escolher_tarefa(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return None

    listar_tarefas(tarefas)

    try:
        escolha = int(input("Digite o número da tarefa: "))
        indice = escolha - 1

        tarefas[indice]

        return indice

    except ValueError:
        print("Digite um número válido.")
        return None

    except IndexError:
        print("Tarefa inválida.")
        return None


def marcar_tarefa_concluida(tarefas):
    indice = escolher_tarefa(tarefas)

    if indice is None:
        return

    tarefas[indice].marcar_como_concluida()
    salvar_tarefas(tarefas)

    print("Tarefa marcada como concluída.")


def remover_tarefa(tarefas):
    indice = escolher_tarefa(tarefas)

    if indice is None:
        return

    tarefa_removida = tarefas.pop(indice)
    salvar_tarefas(tarefas)

    print(f"Tarefa '{tarefa_removida.titulo}' removida.")


def listar_tarefas_pendentes(tarefas):
    pendentes = []

    for tarefa in tarefas:
        if not tarefa.concluida:
            pendentes.append(tarefa)

    if not pendentes:
        print("Nenhuma tarefa pendente.")
        return

    print("\nTarefas pendentes:")

    for indice, tarefa in enumerate(pendentes, start=1):
        print(
            f"{indice}. {tarefa.titulo} "
            f"- Prioridade: {tarefa.prioridade} "
            f"- Categoria: {tarefa.categoria}"
        )


def listar_tarefas_concluidas(tarefas):
    concluidas = []

    for tarefa in tarefas:
        if tarefa.concluida:
            concluidas.append(tarefa)

    if not concluidas:
        print("Nenhuma tarefa concluída.")
        return

    print("\nTarefas concluídas:")

    for indice, tarefa in enumerate(concluidas, start=1):
        print(
            f"{indice}. {tarefa.titulo} "
            f"- Prioridade: {tarefa.prioridade} "
            f"- Categoria: {tarefa.categoria}"
        )


def buscar_tarefa(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    termo = input("Digite uma palavra para buscar: ").strip().lower()

    if not termo:
        print("Digite uma palavra válida.")
        return

    encontradas = []

    for tarefa in tarefas:
        titulo = tarefa.titulo.lower()
        categoria = tarefa.categoria.lower()

        if termo in titulo or termo in categoria:
            encontradas.append(tarefa)

    if not encontradas:
        print("Nenhuma tarefa encontrada.")
        return

    print("\nTarefas encontradas:")

    for indice, tarefa in enumerate(encontradas, start=1):
        status = "Concluída" if tarefa.concluida else "Pendente"

        print(
            f"{indice}. {tarefa.titulo} - {status} "
            f"- Prioridade: {tarefa.prioridade} "
            f"- Categoria: {tarefa.categoria}"
        )


def executar_programa():
    tarefas = carregar_tarefas()

    while True:
        mostrar_menu()

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            criar_tarefa(tarefas)

        elif opcao == "2":
            listar_tarefas(tarefas)

        elif opcao == "3":
            marcar_tarefa_concluida(tarefas)

        elif opcao == "4":
            remover_tarefa(tarefas)

        elif opcao == "5":
            listar_tarefas_pendentes(tarefas)

        elif opcao == "6":
            listar_tarefas_concluidas(tarefas)

        elif opcao == "7":
            buscar_tarefa(tarefas)

        elif opcao == "8":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")


executar_programa()