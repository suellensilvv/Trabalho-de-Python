import os

def clear_console():
    # Limpa o console
    os.system('cls' if os.name == 'nt' else 'clear')

def display_hangman(tries):
    stages = [  # estágio final: cabeça, tronco, ambos os braços, e ambas as pernas
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # cabeça, tronco, ambos os braços, e uma perna
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # cabeça, tronco, e ambos os braços
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # cabeça, tronco, e um braço
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # cabeça e tronco
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # cabeça
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio inicial
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def get_word():
    return input("Digite a palavra para o jogo da forca: ").upper()

def play(word):
    word_completion = "_" * len(word)  # substitui letras por _
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Vamos jogar Forca!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Por favor, adivinhe uma letra ou palavra: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Você já adivinhou a letra", guess)
            elif guess not in word:
                print(guess, "não está na palavra.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Boa, ", guess, "está na palavra!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Você já adivinhou a palavra", guess)
            elif guess != word:
                print(guess, "não é a palavra.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Palpite inválido.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Parabéns, você adivinhou a palavra! Você venceu!")
    else:
        print("Desculpe, você ficou sem tentativas. A palavra era " + word + ". Talvez da próxima vez!")

def main():
    word = get_word()
    clear_console()
    play(word)

if __name__ == "__main__":
    main()
