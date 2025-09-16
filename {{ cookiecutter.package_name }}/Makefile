.DEFAULT_GOAL := help
.PHONY: docs
SRC_DIRS = ./{{ cookiecutter.module_name }}

# Warning: These checks are not necessarily run on every PR.
test: test-lint test-types test-format  # Run some static checks.

test-format: ## Run code formatting tests
	ruff format --check --diff ${SRC_DIRS}

test-lint: ## Run code linting tests
	ruff check ${SRC_DIRS}

test-types: ## Run type checks.
	mypy --exclude=templates --ignore-missing-imports --implicit-reexport --strict ${SRC_DIRS}

format: ## Format code
	ruff format ${SRC_DIRS}

fix-lint: ## Fix lint errors automatically
	ruff check --fix ${SRC_DIRS}

version: ## Print the current tutor-cairn version
	@python -c 'import io, os; about = {}; exec(io.open(os.path.join("{{ cookiecutter.module_name }}", "__about__.py"), "rt", encoding="utf-8").read(), about); print(about["__version__"])'

ESCAPE = 
help: ## Print this help
	@grep -E '^([a-zA-Z_-]+:.*?## .*|######* .+)$$' Makefile \
		| sed 's/######* \(.*\)/@               $(ESCAPE)[1;31m\1$(ESCAPE)[0m/g' | tr '@' '\n' \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[33m%-30s\033[0m %s\n", $$1, $$2}'
