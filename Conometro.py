import time

def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def start_timer():
    start_time = time.time()
    print("Cronômetro iniciado. Pressione Enter para pausar.")
    while True:
        elapsed_time = time.time() - start_time
        print(f"Tempo decorrido: {format_time(elapsed_time)}", end="\r")
        if input() == "":
            break
    elapsed_time = time.time() - start_time
    print("\nCronômetro pausado.")
    print(f"Tempo final: {format_time(elapsed_time)}")

def main():
    input("Pressione Enter para iniciar o cronômetro...")
    start_timer()

if __name__ == "__main__":
    main()
