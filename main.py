import threading
import time
import csv
import os

from downloader import Downloader
from fake_server import get_file_list
from logger import log

def run(num_threads=4, benchmark=False):
    files = get_file_list()
    threads = []

    if benchmark:
        start_time = time.perf_counter()

    log("Downloads started...")

    for i in range(num_threads):
        downloader = Downloader(name=f"Thread-{i+1}", files=files)
        thread = threading.Thread(target=downloader.run)
        thread.start()
        threads.append(thread)

    for i, thread in enumerate(threads):
        log(f"Waiting Thread-{i+1}...")
        thread.join()
        log(f"Thread-{i+1} finished.")

    log("All downloads have been completed!")

    if benchmark:
        elapsed = time.perf_counter() - start_time
        log(f"⏱ Benchmark: {num_threads} thread(s) completed in {elapsed:.2f} seconds.")

        csv_path = "benchmark_results.csv"
        write_header = not os.path.exists(csv_path)

        with open(csv_path, mode="a", newline="") as csv_file:
            writer = csv.writer(csv_file)
            if write_header:
                writer.writerow(["threads", "total_time"])
            writer.writerow([num_threads, round(elapsed, 2)])
