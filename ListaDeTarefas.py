def display_tasks(tasks):
    if not tasks:
        print("A lista de tarefas está vazia.")
    else:
        print("Tarefas:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    task = input("Digite a tarefa que deseja adicionar: ")
    tasks.append(task)
    print(f"Tarefa '{task}' adicionada com sucesso!")

def remove_task(tasks):
    display_tasks(tasks)
    try:
        task_index = int(input("Digite o número da tarefa que deseja remover: "))
        if 1 <= task_index <= len(tasks):
            removed_task = tasks.pop(task_index - 1)
            print(f"Tarefa '{removed_task}' removida com sucesso!")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

def main():
    tasks = []

    while True:
        print("\nLista de Tarefas")
        print("1. Exibir tarefas")
        print("2. Adicionar tarefa")
        print("3. Remover tarefa")
        print("4. Sair")

        choice = input("Escolha uma opção (1/2/3/4): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Saindo da lista de tarefas. Até mais!")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
