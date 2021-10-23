install:
	pip install -e .[dev]

test:
	pytest

train:
	python -m sample_sklearn.train

clean:
	rm -rf .pytest_cache
	rm -rf src/sample_sklearn/__pycache__/
	rm -rf src/sample_sklearn.egg-info/
	rm -rf tests/__pycache__/