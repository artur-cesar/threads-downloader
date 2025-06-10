

import time
from fake_server import get_file_list, simulate_download


def test_get_file_list_should_returns_20_files():
    files = get_file_list()

    assert isinstance(files, list)
    assert len(files) == 20
    assert all(isinstance(f, str) and f.endswith(".txt") for f in files)

def test_simulated_download_should_finish_in_time_range():
    start = time.perf_counter()
    resut = simulate_download("file_test.txt")
    elapsed = time.perf_counter() - start

    assert resut.startswith("File file_test.txt downloaded in")
    assert 0.5 <= elapsed <= 2.1

