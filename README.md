# Cherry Servers Python SDK

[![codecov](https://codecov.io/gh/cherryservers/cherryservers-sdk-python/graph/badge.svg?token=tQY8jXwiZS)](https://codecov.io/gh/cherryservers/cherryservers-sdk-python)
[![unit-test](https://github.com/cherryservers/cherryservers-sdk-python/actions/workflows/unit-test.yml/badge.svg)](https://github.com/cherryservers/cherryservers-sdk-python/actions/workflows/unit-test.yml)
[![lint](https://github.com/cherryservers/cherryservers-sdk-python/actions/workflows/lint.yml/badge.svg)](https://github.com/cherryservers/cherryservers-sdk-python/actions/workflows/lint.yml)
[![Documentation Status](https://readthedocs.org/projects/cherryservers-sdk-python/badge/?version=latest)](https://cherryservers-sdk-python.readthedocs.io/en/latest/?badge=latest)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cherryservers-sdk-python?pypiBaseUrl=https%3A%2F%2Ftest.pypi.org)

Cherry Servers Python library for resource management.

The documentation for this library is available at https://cherryservers-sdk-python.readthedocs.io.
The documentation for the Cherry Servers API can be found at https://api.cherryservers.com/doc/.

## Usage

The preferred way to install this package is with pip:

```sh
pip install cherryservers-sdk-python
```

A simple example of how to provision a server and print its information:

```python
import cherryservers_sdk_python

facade = cherryservers_sdk_python.facade.CherryApiFacade(token="my-token")

# Create a server.
creation_req = cherryservers_sdk_python.servers.CreationRequest(
    region="LT-Siauliai", plan="B1-1-1gb-20s-shared"
)
server = facade.servers.create(creation_req, project_id=220189)

print(server.get_model())
```
For more examples, check out the [documentation](https://cherryservers-sdk-python.readthedocs.io).

## Development

### Requirements

* Python version >= 3.10
* [poetry](https://python-poetry.org/) version >= 2.0.0

### Setup

1. Clone the repository with:
```sh
git clone git@github.com:caliban0/cherryservers-sdk-python.git
cd cherryservers-sdk-python
```
2. Install package dependencies:
```sh
poetry install --with dev
```
If ran from inside a virtual environment, poetry should detect and use it.
Otherwise, it will create a new one, which you can activate with:
```sh
eval $(poetry env activate)
```
It's also highly recommended to set up [`pre-commit`](https://pre-commit.com/):
```sh
pre-commit install
```

### Testing

Run unit tests:
```sh
pytest tests/unit
```

Running integration tests requires the following environment variables to be set:
1. CHERRY_TEST_API_KEY - your Cherry Servers API key.
2. CHERRY_TEST_TEAM_ID - the team for which the resources will be provisioned.
3. CHERRY_TEST_BAREMETAL_SERVER_ID -  pre-existing baremetal server, for storage testing.

WARNING: running integration tests consumes real resources and will incur costs!

Run integration tests:
```sh
pytest tests/integration
```

## Release

1. Update version in `pyproject.toml`.
2. Update version in `cherryservers_sdk_python/_version.py`.
3. Run `git cliff -o CHANGELOG.md  --tag {version}` to generate the changelog.
4. Create a GitHub release.
