.PHONY: generate-plugin-for-tests help test test-plugin test-plugin-install \
        test-plugin-quality
.DEFAULT_GOAL := help

MSG:=\e[1;34m>> # Enable bold-blue text and prefix with >>.
END_MSG:=\e[0m  # Turn off text decoration.

# Warning: These checks are not yet run on every PR.
# We will add them to CI as part of https://github.com/overhangio/cookiecutter-tutor-plugin/issues/7.
test: generate-plugin-for-tests test-plugin   ## Runs all checks for this repo.

generate-plugin-for-tests:  ## Generate a plugin using the cookiecutter defaults.
	@echo "$(MSG)Generating a plugin with default parameters, for testing...$(END_MSG)"
	rm -rf tutor-contrib-myplugin
	cookiecutter --no-input .
	# The cookiecutter has many example code blocks prefixed with '### '.
	# To help ensure that the example code would work if the user uncommented it,
	# we remove the all '### ' occurances before running tests.
	sed -i 's/### //' tutor-contrib-myplugin/tutormyplugin/plugin.py
	# We must also create this init task template, which the cookiecutter
	# doesn't generate because its usage in plugin.py is commented out.
	touch tutor-contrib-myplugin/tutormyplugin/templates/myplugin/tasks/lms/init.sh
	@echo "$(MSG)Plugin generated.$(END_MSG)"

test-plugin: test-plugin-quality test-plugin-install  ## Test the default plugin.

test-plugin-quality:  ## Run static checks on the default plugin.
	@echo "$(MSG)Running static checks on the generated plugin...$(END_MSG)"
	cd tutor-contrib-myplugin && make test
	@echo "$(MSG)Static checks on the generated plugin passed.$(END_MSG)"

test-plugin-install:  ## Smoke-test that the default plugin works with Tutor.
	@echo "$(MSG)Testing that the generated plugin can be installed, enabled, and used in Tutor...$(END_MSG)"
	pip install -e tutor-contrib-myplugin
	tutor plugins enable myplugin
	tutor config save
	tutor myplugin example-command # This should just print a line and exit 0.
	@echo "$(MSG)It seems like the generated plugin works with Tutor.$(END_MSG)"

ESCAPE = 
help: ## Print this help
	@grep -E '^([a-zA-Z_-]+:.*?## .*|######* .+)$$' Makefile \
		| sed 's/######* \(.*\)/@               $(ESCAPE)[1;31m\1$(ESCAPE)[0m/g' | tr '@' '\n' \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[33m%-30s\033[0m %s\n", $$1, $$2}'
