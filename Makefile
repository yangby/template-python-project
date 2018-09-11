SRC_DIR = fibonacci
RM = rm -f

install-deps:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

pep8-check:
	yapf --recursive --parallel --style pep8 --diff .

pep8-fix:
	yapf --recursive --parallel --style pep8 --in-place .

pep257-check:
	pydocstyle --explain .

lint-check:
	find . -iname "*.py" \
		| xargs pylint \
			--suggestion-mode=y --output-format=colorized --reports=n --score=y

security-check:
	safety check --bare --full-report
	bandit --recursive --format screen ${SRC_DIR}

test: clean-build
	python -m pytest \
		--maxfail=0 --color=yes \
		--hypothesis-show-statistics \
		--benchmark-skip \
		tests/

coverage: clean-build clean-coverage
	coverage run --source ${SRC_DIR} --module pytest \
		--pythonwarnings=default:::fibonacci \
		--benchmark-skip
	coverage report --skip-covered --show-missing

bench: clean-build
	python -m pytest \
		--maxfail=0 --color=yes \
		--pythonwarnings=default:::fibonacci \
		--benchmark-only \
		benches/

clean: clean-build clean-coverage clean-package

clean-build:
	-find . -type d -name '__pycache__' | xargs -I {} ${RM} -r {}
	-${RM} -r .pytest_cache .hypothesis .benchmarks

clean-coverage:
	coverage erase

clean-package:
	-${RM} -r build *.egg-info dist
