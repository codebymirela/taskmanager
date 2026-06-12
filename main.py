import json


def carregar_tarefas():
    try:
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []


def salvar_tarefas(tarefas):
    with open("tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)


tarefas = carregar_tarefas()

while True:
    print("\n=== Gerenciador de Tarefas ===")
    print("1. Criar tarefa")
    print("2. Listar tarefa")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Digite o título da tarefa: ")

        tarefa = {
            "titulo": titulo,
            "concluida": False
        }

        tarefas.append(tarefa)
        salvar_tarefas(tarefas)

        print("Tarefa criada com sucesso.")

    elif opcao == "2":
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nSuas tarefas:")

            for indice, tarefa in enumerate(tarefas, start=1):
                status = "Concluída" if tarefa["concluida"] else "Pendente"
                print(f"{indice}. {tarefa['titulo']} - {status}")

    elif opcao == "3":
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nSuas tarefas:")

            for indice, tarefa in enumerate(tarefas, start=1):
                status = "Concluída" if tarefa["concluida"] else "Pendente"
                print(f"{indice}. {tarefa['titulo']} - {status}")

            try:
                escolha = int(input("Digite o número da tarefa concluída: "))
                indice = escolha - 1

                tarefas[indice]["concluida"] = True
                salvar_tarefas(tarefas)

                print("Tarefa marcada como concluída.")
            except ValueError:
                print("Digite um número válido.")
            except IndexError:
                print("Tarefa inválida.")

    elif opcao == "4":
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nSuas tarefas:")

            for indice, tarefa in enumerate(tarefas, start=1):
                status = "Concluída" if tarefa["concluida"] else "Pendente"
                print(f"{indice}. {tarefa['titulo']} - {status}")

            try:
                escolha = int(input("Digite o número da tarefa que deseja remover: "))
                indice = escolha - 1

                tarefa_removida = tarefas.pop(indice)
                salvar_tarefas(tarefas)

                print(f"Tarefa '{tarefa_removida['titulo']}' removida.")
            except ValueError:
                print("Digite um número válido.")
            except IndexError:
                print("Tarefa inválida.")

    elif opcao == "5":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")