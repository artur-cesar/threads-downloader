

run:
	python cli.py --threads 4

run-threads:
	python cli.py --threads $(T)

benchmark:
	python cli.py --threads 4 --benchmark

benchmark-threads:
	python cli.py --threads $(T) --benchmark
plot:
	python plot_benchmark.py