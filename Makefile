run:
	uvicorn --reload src.application.server:app --host 0.0.0.0 --port 5000

commit:
	pytest src/test/unit
	pytest src/test/functional
	pre-commit run
	gitmoji -c

install:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install -e .
