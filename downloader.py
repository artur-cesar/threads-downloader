from fake_server import simulate_download
from logger import log
import threading


class Downloader:
    def __init__(self, name: str, files: list[str]):
        self.name = name
        self.files = files
        self.lock = threading.Lock()

    #TODO: refactor this using with.
    def run(self):
        while True:
            self.lock.acquire()
            if not self.files:
                self.lock.release()
                break

            file_name = self.files.pop(0)
            self.lock.release()

            log(f"{self.name} está baixando {file_name}...")
            content = simulate_download(file_name)
            log(f"{self.name} finished {file_name}: {content[:40]}...")