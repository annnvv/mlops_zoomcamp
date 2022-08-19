# Best Pratices

## Unit Testing - pytest

- Need to have separate `tests` folder
- Need to have an empty `__init__.py` in the `tests` folder so that Python knows that there are modules (see around minute 8 of video 6.1)
- the point of unit testing is to test individual functions, that we get the expected output from each function 

## Command line - pytest
See [pytest invokation documentation](https://docs.pytest.org/en/7.1.x/how-to/usage.html)
```
pipenv run pytest tests 
```


## Integration Testing



# Module 6.4
## Linting - pylint 
pylint documentation [here](https://pylint.pycqa.org/en/latest/)

Pylint checks for errors, tries to enforce a coding standard, and looks for code smells.

Note that Pylint prefixes each of the problem areas with a R, C, W, E, or F, meaning:
- [R]efactor for a “good practice” metric violation
- [C]onvention for coding standard violation
- [W]arning for stylistic problems, or minor programming issues
- [E]rror for important programming issues (i.e. most probably bug)
- [F]atal for errors which prevented further processing

You can configure pylint with a `.pylintrc` file. See [here](https://www.codeac.io/documentation/pylint-configuration.html) 
(Configuration can be set in `pyproject.toml`, an alternative to having many config files, created with `PEP-518`)

Pylint is meant to be called from the command line. `pylint --recursive=y .`
- can suppress warning locally for a specific class or method with `#pylint: disable=too-few-public-methods`

## Formatting - black

CLI commands: 
to see the issues: `black --diff --skip-string-normalization . | less`
to apply changes: `black --skip-string-normalization .`
Add trailing commas to prevent black from making things single line

Can add black configuration with `pyproject.toml`

## Sorting imports - isort
isort re-arranges import statements based on Python convention 

CLI commands:
to see the issues: `isort --diff. `
to apply changes: `isort .`

Can add isort configuration with `pyproject.toml`

# Module 6.5
## Pre-commit hooks - pre-commit
pre-commit documentation [here](https://pre-commit.com/)

Precommit hooks are specified in a `.pre-commit-config.yaml` file. 
For supported python pre-commit hooks, see [here](https://pre-commit.com/hooks.html)

Once you have the `.pre-commit-config.yaml`, install the precommit hooks using the CLI command: `pre-commit install`. pre-commit will run automatically on git commits.
Or you can run pre-commit on all files (optional) using the CLI command `pre-commit run --all-files` 

# Module 6.6
## Make and Makefiles
