#!/bin/bash
mkdir -p build
env/bin/mypy --junit-xml=build/python-mypy.xml --ignore-missing-imports example ||:
env/bin/pylint --reports=n --rcfile=config/pylint.rc --output-format=parseable example/*/ > build/python-lint.txt ||:
env/bin/nosetests example --with-xunit --xunit-file=build/python-tests.xml --with-coverage --cover-xml --cover-xml-file=build/python-coverage.xml ||:
