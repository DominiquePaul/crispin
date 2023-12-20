.PHONY: test

test:
	pytest

update_pkg:
	python setup.py sdist
	python setup.py bdist_wheel
	twine upload dist/*

