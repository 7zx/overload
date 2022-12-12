download:

	@echo
	@echo ---------------------------------
	@echo ------- Installing Poetry -------
	@echo ---------------------------------
	@echo

	@curl -sSL https://install.python-poetry.org | python3 -

install: 

	@echo
	@echo ---------------------------------
	@echo ---- Installing dependencies ----
	@echo ---------------------------------
	@echo
	
	@poetry install --without dev

run:

	@echo
	@echo ---------------------------------
	@echo - Activating Virtual Enviroment -
	@echo ---------------------------------
	@echo

	@poetry run python3 overload.py

server:

	@echo
	@echo ---------------------------------
	@echo ------ Server is Listening ------
	@echo ---------------------------------
	@echo

	@cd tools/dev && python3 server.py

sniff:

	@echo
	@echo ---------------------------------
	@echo ----- Starting TCP Sniffing -----
	@echo ---------------------------------
	@echo

	@cd tools/dev && sudo python3 sniff.py

setup: download install 
