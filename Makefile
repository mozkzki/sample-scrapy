.PHONY: black flake8 ut clear start1 start2

all: lint ut

start: clear start1 start2

lint: flake8 black

black:
	black .

flake8:
	flake8 --max-line-length=100 --ignore=E203,W503 ./main

ut:
	pytest -v --capture=no --cov-config .coveragerc --cov=main --cov-report=xml --cov-report=term-missing .

clear:
	rm -rf ./main/out

start1:
	cd main && scrapy crawl topics -o ./out/topics.csv && cd .

start2:
	cd main && scrapy crawl news_crawl -o ./out/news_crawl.csv && cd .