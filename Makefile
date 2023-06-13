.DEFAULT_GOAL := help

ifeq ($(OS),Windows_NT)
	export CREATE_DIST=if not exist dist mkdir dist
	export DELETE_DIST_BUILD=if exist build rd /s /q build
	export DELETE_DIST_WHEEL=del /f /q dist\\*.whl
	export DELETE_SPHINX_1=del /f /q docs\\build\\* docs\\source\\sua.rst docs\\source\\sua.vector3d.rst
	export DELETE_SPHINX_2=del /f /q docs\\source\\modules.rst
	export ENV_FOR_DYNACONF=test
	export OPTION_NUITKA=
	export PIPENV=python -m pipenv
	export PYTHON=python
	export PYTHONPATH=src
	export PYTHONPATH_PYTEST=src
	export PYTHONPATH_SUA=src\\sua
	export PYTHONPATH_TESTS=tests
	export SETUP=${PYTHON} src\\setup.py
	export SPHINX_BUILDDIR=docs\\build
	export SPHINX_SOURCEDIR=docs\\source
	export VSCODE=code
else
	export CREATE_DIST=mkdir -p dist
	export DELETE_DIST_BUILD=rm -rf build
	export DELETE_DIST_WHEEL=rm -rf dist/*.whl
	export DELETE_SPHINX_1=rm -rf docs/build/* docs/source/sua.rst docs/source/sua.vector3d.rst
	export DELETE_SPHINX_2=rm -rf docs/source/modules.rst
	export ENV_FOR_DYNACONF=test
	export OPTION_NUITKA=--disable-ccache
	export PIPENV=python3 -m pipenv
	export PYTHON=python3
	export PYTHONPATH=src
	export PYTHONPATH_PYTEST=src
	export PYTHONPATH_SUA=src/sua
	export PYTHONPATH_TESTS=tests
	export SETUP=${PYTHON} src/setup.py
	export SPHINX_BUILDDIR=docs/build
	export SPHINX_SOURCEDIR=docs/source
	export VSCODE=code
endif

##                                                                            .
## =============================================================================
## SUA - Template Library - make Documentation.
##       -----------------------------------------------------------------------
##       The purpose of this Makefile is to support the whole software
##       development process for sua. It contains also the necessary
##       tools for the CI activities.
##       -------------------------------------------------------------
##       The available make commands are:
## ------------------------------------------------------------------------------
## help:               Show this help.
## -----------------------------------------------------------------------------
## app-dev:            Setup the environment for developing apps.
app-dev: vscode
## build:              Build the application.
build: build-python build-rust
## build-python        Build the Python application.
build-python: compileall nuitka wheel
## build-rust:         Build the Rust application.
build-rust: cargo-build
## dev:                Format, lint and test the code.
dev: dev-python dev-rust
## dev-python          Format, lint and test the Python code.
dev-python: format-python lint-python tests-python
## dev-rust:           Format, lint and test the Rust code.
dev-rust: format-rust lint-rust tests-rust
## docs:               Check the documentation.
docs: docs-python docs-rust
## docs-python:        Check the API documentation, create and upload the Python user documentation.
docs-python: pydocstyle sphinx
## docs-rust:          Check the API documentation, create and upload the Rust user documentation.
docs-rust: cargo-docs
## final:              Format, lint and test the codel.
final: final-python final-rust
## final_python:       Format, lint and test the Python code, create a ddl, the documentation and a wheel.
final-python: dev-python docs-python build-python
## final_rust:         Format, lint and test the Rust code, create the documentation.
final-rust: dev-rust docs-rust build-rust
## format:             Format the Python code and the Rust code.
format: format-python format-rust
## format-python:      Format the Python code with isort, Black and docformatter.
format-python: isort black docformatter
## format-rust:        Format the Rust code with rustfmt.
format-rust: cargo-fmt
## lint:               Lint the Python code and the Rust code.
lint: lint-python lint-rust
## lint-python:        Lint the Python code with Bandit, Flake8, Pylint and Mypy.
lint-python: bandit flake8 pylint mypy
## lint-rust:          Lint the Rust code with cargo clippy.
lint-rust: cargo-clippy
## tests:              Run all Python tests and Rust tests.
tests: tests-python tests-rust
## tests-python:       Run all Python tests with pytest.
tests-python: pytest
## tests-rust:         Run all Rust tests with cargo test.
tests-rust: cargo-test
## -----------------------------------------------------------------------------

help:
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

# Bandit is a tool designed to find common security issues in Python code.
# https://github.com/PyCQA/bandit
# Configuration file: none
bandit:             ## Find common security issues with Bandit.
	@echo Info **********  Start: Bandit ***************************************
	@echo PYTHON          =${PYTHON}
	@echo PYTHONPATH      =${PYTHONPATH}
	@echo PYTHONPATH_TESTS=${PYTHONPATH_TESTS}
	${PIPENV} run bandit --version
	@echo ----------------------------------------------------------------------
	${PIPENV} run bandit -c pyproject.toml -r ${PYTHONPATH}
	@echo Info **********  End:   Bandit ***************************************

# The Uncompromising Code Formatter
# https://github.com/psf/black
# Configuration file: pyproject.toml
black:              ## Format the Python code with Black.
	@echo Info **********  Start: black ****************************************
	@echo PYTHON          =${PYTHON}
	@echo PYTHONPATH      =${PYTHONPATH}
	@echo PYTHONPATH_TESTS=${PYTHONPATH_TESTS}
	${PIPENV} run black --version
	@echo ----------------------------------------------------------------------
	${PIPENV} run black ${PYTHONPATH} ${PYTHONPATH_TESTS}
	@echo Info **********  End:   black ****************************************

cargo-build:        ## Build the Rust application.
	@echo Info **********  Start: build ***************************************
	cargo build
	@echo Info **********  End:   build ***************************************

cargo-clippy:       ## Lint Rust code with clippy.
	@echo Info **********  Start: clippy **************************************
	cargo clippy --version
	@echo ----------------------------------------------------------------------
	cargo clippy --all-targets --all-features -- -D warnings
	@echo Info **********  End:   clippy **************************************

cargo-docs:         ## Document Rust code with doc.
	@echo Info **********  Start: doc *****************************************
	cargo doc
	@echo Info **********  End:   doc *****************************************

cargo-fmt:          ## Format Rust code with rustfmt.
	@echo Info **********  Start: rustfmt *************************************
	cargo fmt --version
	@echo ----------------------------------------------------------------------
	cargo fmt --check --verbose
	@echo Info **********  End:   rustfmt *************************************

cargo-test:         ## Test Rust code with test.
	@echo Info **********  Start: test ****************************************
	cargo test
	@echo Info **********  End:   test ****************************************

# Byte-compile Python libraries
# https://docs.python.org/3/library/compileall.html
# Configuration file: none
compileall:         ## Byte-compile the Python libraries.
	@echo Info **********  Start: Compile All Python Scripts ******************
	@echo PYTHON    =${PYTHON}
	@echo PYTHONPATH=${PYTHONPATH}
	${PYTHON} --version
	@echo ---------------------------------------------------------------------
	${PYTHON} -m compileall
	@echo Info **********  End:   Compile All Python Scripts ******************

# Python interface to coveralls.io API
# https://github.com/TheKevJames/coveralls-python
# Configuration file: none
coveralls:          ## Run all the tests and upload the coverage data to coveralls.
	@echo Info **********  Start: coveralls ***********************************
	@echo PYTHON    =${PYTHON}
	@echo PYTHONPATH=${PYTHONPATH}
	@echo ---------------------------------------------------------------------
	${PIPENV} run pytest --cov=${PYTHONPATH} --cov-report=xml tests
	@echo ----------------------------------------------------------------------
	${PIPENV} run coveralls --service=github
	@echo Info **********  End:   coveralls ***********************************

# Formats docstrings to follow PEP 257
# https://github.com/PyCQA/docformatter
# Configuration file: none
docformatter:       ## Format the docstrings in the Python code with docformatter.
	@echo Info **********  Start: docformatter ********************************
	@echo PYTHON        =${PYTHON}
	@echo PYTHONPATH    =${PYTHONPATH}
	${PIPENV} run docformatter --version
	@echo ----------------------------------------------------------------------
	${PIPENV} run docformatter --in-place -r ${PYTHONPATH}
	@echo Info **********  End:   docformatter ********************************

# Flake8: Your Tool For Style Guide Enforcement.
# https://github.com/pycqa/flake8
# Configuration file: cfg.cfg
flake8:             ## Enforce the Python Style Guides with Flake8.
	@echo Info **********  Start: Flake8 **************************************
	@echo PYTHON          =${PYTHON}
	@echo PYTHONPATH      =${PYTHONPATH}
	@echo PYTHONPATH_TESTS=${PYTHONPATH_TESTS}
	${PIPENV} run flake8 --version
	@echo ----------------------------------------------------------------------
	${PIPENV} run flake8 ${PYTHONPATH}
	@echo Info **********  End:   Flake8 **************************************

# isort your imports, so you don't have to.
# https://github.com/PyCQA/isort
# Configuration file: pyproject.toml
isort:              ## Edit and sort the imports in the Python code with isort.
	@echo Info **********  Start: isort ***************************************
	@echo PYTHON          =${PYTHON}
	@echo PYTHONPATH      =${PYTHONPATH}
	@echo PYTHONPATH_TESTS=${PYTHONPATH_TESTS}
	${PIPENV} run isort --version
	@echo ----------------------------------------------------------------------
	${PIPENV} run isort ${PYTHONPATH} ${PYTHONPATH_TESTS}
	@echo Info **********  End:   isort ***************************************

# Mypy: Static Typing for Python
# https://github.com/python/mypy
# Configuration file: pyproject.toml
mypy:               ## Find typing issues with Mypy.
	@echo Info **********  Start: Mypy ****************************************
	@echo PYTHON          =${PYTHON}
	@echo PYTHONPATH      =${PYTHONPATH}
	@echo PYTHONPATH_TESTS=${PYTHONPATH_TESTS}
	${PIPENV} run mypy --version
	@echo ----------------------------------------------------------------------
	${PIPENV} run mypy ${PYTHONPATH}
	@echo Info **********  End:   Mypy ****************************************

# Nuitka: Python compiler written in Python
# https://github.com/Nuitka/Nuitka
nuitka:             ## Create a dynamic link library.
	@echo Info **********  Start: nuitka **************************************
	@echo CREATE_DIST   =${CREATE_DIST}
	@echo PYTHON        =${PYTHON}
	@echo PYTHONPATH    =${PYTHONPATH}
	@echo PYTHONPATH_SUA=${PYTHONPATH}
	${PIPENV} run ${PYTHON} -m nuitka --version
	@echo ---------------------------------------------------------------------
	${CREATE_DIST}
	${PIPENV} run ${PYTHON} -m nuitka ${OPTION_NUITKA} --include-package=sua --module ${PYTHONPATH_SUA} --no-pyi-file --output-dir=dist --remove-output
	@echo Info **********  End:   nuitka **************************************

# pip is the package installer for Python.
# https://pypi.org/project/pip/
# Configuration file: none
# Pipenv: Python Development Workflow for Humans.
# https://github.com/pypa/pipenv
# Configuration file: Pipfile
pipenv-dev:         ## Install the package dependencies for development.
	@echo Info **********  Start: Installation of Development Packages ********
	@echo PYTHON    =${PYTHON}
	@echo PYTHONPATH=${PYTHONPATH}
	@echo ----------------------------------------------------------------------
	${PYTHON} -m pip install --upgrade pip
	${PYTHON} -m pip install --upgrade pipenv
	${PYTHON} -m pip uninstall -y virtualenv
	${PYTHON} -m pip install virtualenv
	${PIPENV} install
	${PIPENV} --rm
	${PIPENV} install --dev
	${PIPENV} update --dev
	@echo ----------------------------------------------------------------------
	${PIPENV} run pip freeze
	@echo ----------------------------------------------------------------------
	${PYTHON} --version
	${PYTHON} -m pip --version
	${PYTHON} -m pipenv --version
	@echo Info **********  End:   Installation of Development Packages ********
pipenv-prod:        ## Install the package dependencies for production.
	@echo Info **********  Start: Installation of Production Packages *********
	@echo PYTHON=${PYTHON}
	@echo PYTHONPATH=${PYTHONPATH}
	@echo ----------------------------------------------------------------------
	${PYTHON} -m pip install --upgrade pip
	${PYTHON} -m pip install --upgrade pipenv
	${PYTHON} -m pip uninstall -y virtualenv
	${PYTHON} -m pip install virtualenv
	${PIPENV} install
	${PIPENV} --rm
	${PIPENV} install
	${PIPENV} update
	@echo ----------------------------------------------------------------------
	${PIPENV} run pip freeze
	@echo ----------------------------------------------------------------------
	${PYTHON} --version
	${PYTHON} -m pip --version
	${PYTHON} -m pipenv --version
	@echo Info **********  End:   Installation of Production Packages *********

# pydocstyle - docstring style checker.
# https://github.com/PyCQA/pydocstyle
# Configuration file: pyproject.toml
pydocstyle:         ## Check the API documentation with pydocstyle.
	@echo Info **********  Start: pydocstyle **********************************
	@echo PYTHON    =${PYTHON}
	@echo PYTHONPATH=${PYTHONPATH}
	${PIPENV} run pydocstyle --version
	@echo ----------------------------------------------------------------------
	${PIPENV} run pydocstyle --count --match='(?!PDFLIB\\)*\.py' ${PYTHONPATH}
	@echo Info **********  End:   pydocstyle **********************************

# Pylint is a tool that checks for errors in Python code.
# https://github.com/PyCQA/pylint/
# Configuration file: .pylintrc
pylint:             ## Lint the code with Pylint.
	@echo Info **********  Start: Pylint **************************************
	@echo PYTHON          =${PYTHON}
	@echo PYTHONPATH      =${PYTHONPATH}
	@echo PYTHONPATH_TESTS=${PYTHONPATH_TESTS}
	${PIPENV} run pylint --version
	@echo ----------------------------------------------------------------------
	${PIPENV} run pylint ${PYTHONPATH}
	@echo Info **********  End:   Pylint **************************************

# pytest: helps you write better programs.
# https://github.com/pytest-dev/pytest/
# Configuration file: pyproject.toml
pytest:             ## Run all tests with pytest.
	@echo Info **********  Start: pytest **************************************
	${PIPENV} run pytest --version
	@echo ----------------------------------------------------------------------
	${PIPENV} run pytest --dead-fixtures tests
	${PIPENV} run pytest --cache-clear --cov=${PYTHONPATH_PYTEST} --cov-report term-missing:skip-covered --random-order -v tests
	@echo Info **********  End:   pytest **************************************
pytest-ci:          ## Run all tests with pytest after test tool installation.
	@echo Info **********  Start: pytest **************************************
	${PIPENV} install pytest
	${PIPENV} install pytest-cov
	${PIPENV} install pytest-deadfixtures
	${PIPENV} install pytest-helpers-namespace
	${PIPENV} install pytest-random-order
	@echo ----------------------------------------------------------------------
	${PIPENV} run pytest --version
	@echo ----------------------------------------------------------------------
	${PIPENV} run pytest --dead-fixtures tests
	${PIPENV} run pytest --cache-clear --cov=${PYTHONPATH_PYTEST} --cov-report term-missing:skip-covered -v tests
	@echo Info **********  End:   pytest **************************************
pytest-first-issue: ## Run all tests with pytest until the first issue occurs.
	@echo Info **********  Start: pytest **************************************
	${PIPENV} run pytest --version
	@echo ----------------------------------------------------------------------
	${PIPENV} run pytest --cache-clear --cov=${PYTHONPATH_PYTEST} --cov-report term-missing:skip-covered -rP -v -x tests
	@echo Info **********  End:   pytest **************************************
pytest-issue:       ## Run only the tests with pytest which are marked with 'issue'.
	@echo Info **********  Start: pytest **************************************
	${PIPENV} run pytest --version
	@echo ----------------------------------------------------------------------
	${PIPENV} run pytest --cache-clear --capture=no --cov=${PYTHONPATH_PYTEST} --cov-report term-missing:skip-covered -m issue -rP -v -x tests
	@echo Info **********  End:   pytest **************************************
pytest-module:      ## Run tests of specific module(s) with pytest - test_all & test_cfg_cls_setup & test_db_cls.
	@echo Info **********  Start: pytest **************************************
	${PIPENV} run pytest --version
	@echo ----------------------------------------------------------------------
	${PIPENV} run pytest --cache-clear --cov=${PYTHONPATH_PYTEST} --cov-report term-missing:skip-covered -v tests/test_db_cls_action.py
	@echo Info **********  End:   pytest **************************************

#rust-run:
#    @echo Info **********  Start: Rust Run ************************************
#	@echo ----------------------------------------------------------------------
#	cargo run
#	@echo Info **********  End:   Rust Run ************************************
#
#rust-target:
#	@echo Info **********  Start: Rust Build **********************************
#	@echo ----------------------------------------------------------------------
#	cargo build
#	@echo Info **********  End:   Rust Build **********************************

# sphinx: Python Documentation Generator
# https://github.com/sphinx-doc/sphinx
# https://www.sphinx-doc.org/en/master/
# Configuration file:
#    docs/source/conf.py
# Convert md files to rst format:
#    https://cloudconvert.com/
# Read the Docs:
#    https://readthedocs.org/
# reStructuredText:
#    https://docutils.sourceforge.io/rst.html
# Setup:
#    python -m pipenv run sphinx-quickstart
# Sphinx Themes Gallery:
#    https://sphinx-themes.org/
sphinx:            ##  Create the user documentation with Sphinx.
	@echo Info **********  Start: sphinx **************************************
	@echo PYTHON          =${PYTHON}
	@echo PYTHONPATH_SUA  =${PYTHONPATH_SUA}
	@echo DELETE_SPHINX_1 =${DELETE_SPHINX_1}
	@echo DELETE_SPHINX_2 =${DELETE_SPHINX_2}
	@echo SPHINX_BUILDDIR =${SPHINX_BUILDDIR}
	@echo SPHINX_SOURCEDIR=${SPHINX_SOURCEDIR}
	@echo ---------------------------------------------------------------------
	${DELETE_SPHINX_1}
	cd docs
	${PIPENV} run sphinx-apidoc -o ${SPHINX_SOURCEDIR} ${PYTHONPATH_SUA}
	${DELETE_SPHINX_2}
	${PIPENV} run sphinx-build -M html ${SPHINX_SOURCEDIR} ${SPHINX_BUILDDIR}
#	${PIPENV} run sphinx-build -b rinoh ${SPHINX_SOURCEDIR} ${SPHINX_BUILDDIR}/pdf
	cd ..
	@echo Info **********  End:   sphinx **************************************

version:            ## Show the installed software versions.
	@echo Info **********  Start: version *************************************
	@echo PYTHON    =${PYTHON}
	@echo PYTHONPATH=${PYTHONPATH}
	${PYTHON} -m pip --version
	${PYTHON} -m pipenv --version
	@echo Info **********  End:   version *************************************

# VS Code
# Setup the environment to develop apps using the sua library
# Configuration file: none
vscode:
	@echo Info **********  Start: Setup Code Enviornment ***********************
	@echo PYTHON    =${PYTHON}
	@echo PYTHONPATH=${PYTHONPATH}
	${PYTHON} --version
	@echo ---------------------------------------------------------------------
	${VSCODE} .

# wheel: The official binary distribution format for Python
# https://github.com/pypa/setuptools
# https://github.com/pypa/wheel
# Configuration file: setup.cfg
wheel:              ## Create a distribution archive with a wheel.
	@echo Info **********  Start: wheel ***************************************
	@echo CREATE_DIST=${CREATE_DIST}
	@echo DELETE_DIST=${DELETE_DIST_WHEEL}
	@echo PYTHON     =${PYTHON}
	@echo PYTHONPATH =${PYTHONPATH}
	@echo ---------------------------------------------------------------------
	${CREATE_DIST}
	${DELETE_DIST_BUILD}
	${DELETE_DIST_WHEEL}
	${PIPENV} run ${SETUP} bdist_wheel
	${PIPENV} run unzip -l dist/*.whl
	${PIPENV} run check-wheel-contents dist
	${PIPENV} run ${SETUP} build_ext --inplace
	@echo Info **********  End:   wheel ***************************************

## ============================================================================
