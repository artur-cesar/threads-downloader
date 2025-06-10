import csv
import matplotlib.pyplot as plt

def plot_benchmark(csv_file="benchmark_results.csv"):
    threads = []
    times = []

    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            threads.append(int(row["threads"]))
            times.append(float(row["total_time"]))

    unique = {}
    for t, time in zip(threads, times):
        unique[t] = time

    threads_sorted = sorted(unique.keys())
    times_sorted = [unique[t] for t in threads_sorted]

    plt.figure(figsize=(8, 5))
    plt.bar(threads_sorted, times_sorted, width=0.6)
    plt.title("Benchmark: Threads vs Total Time")
    plt.xlabel("Number of Threads")
    plt.ylabel("Total Time (s)")
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig("benchmark_plot.png")
    plt.show()

if __name__ == "__main__":
    plot_benchmark()
