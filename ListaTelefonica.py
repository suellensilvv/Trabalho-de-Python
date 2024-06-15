def display_contacts(contacts):
    if not contacts:
        print("A lista telefônica está vazia.")
    else:
        print("Lista Telefônica:")
        for name, number in contacts.items():
            print(f"Nome: {name}, Número: {number}")

def add_contact(contacts):
    name = input("Digite o nome do contato: ")
    number = input("Digite o número do contato: ")
    contacts[name] = number
    print(f"Contato '{name}' adicionado com sucesso!")

def remove_contact(contacts):
    name = input("Digite o nome do contato que deseja remover: ")
    if name in contacts:
        del contacts[name]
        print(f"Contato '{name}' removido com sucesso!")
    else:
        print("Contato não encontrado.")

def main():
    contacts = {}

    while True:
        print("\nLista Telefônica")
        print("1. Exibir contatos")
        print("2. Adicionar contato")
        print("3. Remover contato")
        print("4. Sair")

        choice = input("Escolha uma opção (1/2/3/4): ")

        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            remove_contact(contacts)
        elif choice == '4':
            print("Saindo da lista telefônica. Até mais!")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
