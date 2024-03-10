all: lint xword

xword:
	cd project-3-crossword-compiler-bababuck && \
	make LOCAL=1

lint:
	python3 -m flake8
