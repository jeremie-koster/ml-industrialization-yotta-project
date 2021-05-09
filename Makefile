run:
	uvicorn --reload src.application.server:app --host 0.0.0.0 --port 5000

commit:
	pytest src/test/unit
	pre-commit run
	gitmoji -c
