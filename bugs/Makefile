all: update html deploy
deploy: bugs.html template
	cat template bugs.html > ../_pages/outcomes.md

html: bugs.json export.py
	python3 export.py > bugs.html

update:
	python3 retrieve_bug.py > bugs.tmp
	mv bugs.tmp bugs.json
