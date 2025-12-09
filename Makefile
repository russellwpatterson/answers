PYTHON=python3.14

ENV_DIR=.venv

IN_ENV=. $(ENV_DIR)/bin/activate &&

$(ENV_DIR):
	$(PYTHON) -m venv $(ENV_DIR)
	$(IN_ENV) $(PYTHON) -m pip install -U pip pytest

test: $(ENV_DIR)
	$(IN_ENV) pytest .

reset:
	@rm -rf $(ENV_DIR)