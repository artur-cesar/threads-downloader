import time
import random

def get_file_list():
    return [f"file_{i}.txt" for i in range(1, 21)]  # 20 fake files

def simulate_download(file_name: str):
    download_time = random.uniform(0.5, 2.0)  # Mock latency from 0.5 to 2s
    time.sleep(download_time)
    return f"File {file_name} downloaded in {download_time:.2f}s"
