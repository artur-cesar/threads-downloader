from fake_server import simulate_download
from logger import log
import threading


class Downloader:
    def __init__(self, name: str, files: list[str], download_func=None):
        self.name = name
        self.files = files
        self.lock = threading.Lock()
        self.download_func = download_func or simulate_download

    def __get_next_file(self):
        with self.lock:
            if self.files:
                return self.files.pop(0)
            return None


    def run(self):
        while True:
            file_name = self.__get_next_file()
            if not file_name:
                break

            log(f"{self.name} está baixando {file_name}...")
            try:
                content = self.download_func(file_name)
                log(f"{self.name} finished {file_name}: {content[:40]}...")
            except Exception as e:
                log(f"{self.name} erro ao baixar {file_name}: {e}")