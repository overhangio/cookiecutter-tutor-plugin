.PHONY: generate-plugin-for-tests help test test-plugin test-plugin-install \
        test-plugin-quality
.DEFAULT_GOAL := help

# Warning: These checks are not yet run on every PR.
# We will add them to CI as part of https://github.com/overhangio/cookiecutter-tutor-plugin/issues/7).
test: generate-plugin-for-tests test-plugin   ## Runs all checks for this repo.

generate-plugin-for-tests:  ## Generate a plugin using the cookiecutter defaults.
	rm -rf tutor-contrib-myplugin
	cookiecutter --no-input .

test-plugin: test-plugin-quality test-plugin-install  ## Test the default plugin.

test-plugin-quality:  ## Run static checks on the default plugin.
	cd tutor-contrib-myplugin && make test

test-plugin-install:  ## Smoke-test that the default plugin works with Tutor.
	pip install -e tutor-contrib-myplugin
	tutor plugins enable myplugin
	tutor config save
	tutor myplugin example-command # This should just print a line and exit 0.

ESCAPE = 
help: ## Print this help
	@grep -E '^([a-zA-Z_-]+:.*?## .*|######* .+)$$' Makefile \
		| sed 's/######* \(.*\)/@               $(ESCAPE)[1;31m\1$(ESCAPE)[0m/g' | tr '@' '\n' \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[33m%-30s\033[0m %s\n", $$1, $$2}'
