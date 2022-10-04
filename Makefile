download:

	@echo
	@echo ------------------------------------------
	@echo Installing Poetry...
	@echo ------------------------------------------
	@echo

	@curl -sSL https://install.python-poetry.org | python3 -

install: 

	@echo
	@echo ------------------------------------------
	@echo Installing application dependencies...
	@echo ------------------------------------------
	@echo
	
	@poetry install --without dev

run:

	@echo
	@echo ------------------------------------------
	@echo Activating Virtual Enviroment...
	@echo ------------------------------------------
	@echo

	@poetry run python3 overload.py


setup: download install 
