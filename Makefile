PY_SOURCE := $(wildcard *.py)
BIN := .venv/bin
DATABASE := cat.sqlite

initdb:
	-$(RM) $(DATABASE)
	sqlite3 $(DATABASE) < initdb.sql
	sqlite3 $(DATABASE) 'select count(*) from cat'

setup:
	python3 -m venv .venv
	$(BIN)/pip install -U pip wheel
	$(BIN)/pip install -r requirements.txt

run:
	FLASK_APP=webhello.py FLASK_ENV=development $(BIN)/flask run

test:
	pytest -v

fastlint:
	flake8 $(PY_SOURCE)
	@echo DONE

fastlint-safe:
	-flake8 $(PY_SOURCE)

setup-hooks:
	echo 'make pre-commit' > .git/hooks/pre-commit
	chmod +x .git/hooks/pre-commit

pre-commit: fmt fastlint-safe

fmt:
	isort .
	black .

clean:
	-$(RM) -r __pycache__
