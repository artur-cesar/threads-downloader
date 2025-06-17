
from unittest.mock import Mock, patch
from downloader import Downloader

class TestDownloader:

    def test_downloader_should_consume_all_files(self):
        files = [f"file_{i}.txt" for i in range(5)]
        expected = len(files[:])

        mock_download = Mock(side_effect=lambda x: f"{x} - downloaded")

        downloader = Downloader(name="TestThread", files=files, download_func=mock_download)
        downloader.run()

        assert len(files) == 0
        assert mock_download.call_count == expected

    def test_downloader_should_continue_on_download_error(self):
        files = ["file_0.txt", "file_1.txt", "file_2.txt"]

        results = [
            'file_0.txt - ok',
            Exception("simulated failure"),
            "file_2.txt - ok"
        ]

        def side_effect(filename):
            result = results.pop(0)
            if isinstance(result, Exception):
                raise result
            return result
        
        mock_download = Mock(side_effect=side_effect)

        with patch("downloader.log") as mock_log:
            downloader = Downloader(name="Thread-E", files=files, download_func=mock_download)
            downloader.run()

        assert mock_download.call_count == 3