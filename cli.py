import argparse
from main import run

def main():
    parser = argparse.ArgumentParser(description="Simulador de downloads com threads")
    parser.add_argument("--threads", type=int, default=4, help="Número de threads")
    parser.add_argument("--benchmark", action="store_true", help="Exibir tempo total de execução")  # ⬅️ ESTA LINHA
    args = parser.parse_args()

    run(num_threads=args.threads, benchmark=args.benchmark)  # ⬅️ E passe o argumento aqui

if __name__ == "__main__":
    main()
