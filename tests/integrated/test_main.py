import csv
import os

import pytest

from main import run

class TestMain:
    
    @pytest.fixture
    def clean_csv_file(self):
        csv_path = "benchmark_results.csv"
        backup_path = csv_path + ".bak"

        if os.path.exists(csv_path):
            os.rename(csv_path, backup_path)

        yield csv_path

        if os.path.exists(csv_path):
            os.remove(csv_path)
        if os.path.exists(backup_path):
            os.rename(backup_path, csv_path)


    def test_main_should_generates_benchmark_csv(self, clean_csv_file):
        run(num_threads=4, benchmark=True)

        with open(clean_csv_file, newline="") as file:
            reader = list(csv.DictReader(file))
            assert reader, "CSV está vazio"
            last = reader[-1]

            assert int(last["threads"]) == 4
            assert float(last["total_time"]) > 0.0
            