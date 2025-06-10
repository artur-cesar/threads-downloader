import argparse
from main import run

def main():
    parser = argparse.ArgumentParser(description="Thread downloader simulator")
    parser.add_argument("--threads", type=int, default=4, help="Number of threads")
    parser.add_argument("--benchmark", action="store_true", help="Display total execution time")
    args = parser.parse_args()

    run(num_threads=args.threads, benchmark=args.benchmark)

if __name__ == "__main__":
    main()
