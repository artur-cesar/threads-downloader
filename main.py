import threading
import time
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
