# just for CI/CD
#

.PHONY: all test testv build prepare

all:

prepare:
	pip3 install -r requirements.txt

test:
	python3 -m unittest discover tests

testv:
	coverage run -m unittest discover tests
	coverage report
	coverage xml
	out=htmlcov
	coverage html -d "htmlcov";\
	echo "Please visi: http://dev.rexliao.com/htmlcov/"; \


