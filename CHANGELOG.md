# Changelog

All notable changes to this project will be documented in this file.

## [1.1.0] - 2025-07-08

### 🚀 Features

- Add server billing cycle options
- Add py.typed for type checker compatibility

### ⚙️ Miscellaneous Tasks

- Update versions

## [1.0.1] - 2025-06-12

### 🐛 Bug Fixes

- Update region param to 'LT-Siauliai" where relevant
- Change 'cloud_vps_1' to 'B1-1-1gb-20s-shared' in the relevant sections
- Update 'request' library to fix CVE-2024-47081

### 💼 Other

- *(deps)* Bump JRubics/poetry-publish from 2.0 to 2.1

### ⚙️ Miscellaneous Tasks

- Prep for 1.0.1

## [1.0.0] - 2025-01-09

### 🚀 Features

- Add cherry servers api client
- Change user_agent_context to user_agent_suffix
- Add user client
- Rework requests, add ssh keys start, update deps
- Add remaining sshkeys functionality
- Add project management functionality
- Add region management functionality
- Add ip address management functionality
- Add team management functionality
- Add plan management functionality
- Add images management functionality
- Add server management functionality
- Add block storage management functionality
- Prevent attached IP deletion
- Add backup storage functionality
- Move request schemas to resource modules
- Add full message to HTTP/S errors
- Make ssh key model fields optional
- Add ssh key, teams and user integration tests
- Upgrade python dep to 3.12
- Add base classes
- Make user model fields optional
- Make teams model fields optional
- Make server model fields optional
- Make project resource model fields nullable
- Make ip models nullable
- Make image model fields nullable
- Add pricing field to image model
- Make block storage models nullable
- Remove ddos_scrubbing from ips
- Follow redirects manually from now on
- Update block storage model on resize
- Make backup storage model fields nullable
- Rename user agent param
- Add capability to check if resource is deployed
- Add deployment checking capability to backup storages
- Make some server model and reques fields required
- Add status based waiting to server
- Add id getters to all resources
- Add customizable timeouts to all resources

### 🐛 Bug Fixes

- Fully import pricing model, where required
- Add attached server model fields ip getters
- Nullify server model fields
- Fix server dependant model import logic
- Clarify NotBaremetalException error message
- Make id not nullable for region model
- Fix import logic for block_storage
- Fix pricing model import in teams module
- Increase api client delete func timeout to more appropriate
- Fix backup storage deployment condition

### 💼 Other

- Change linter to ruff
- Add PATCH capability to client
- Add pytest dependency
- Update dependencies
- Configure poetry for new package name
- Update dependencies
- Create docs dependency group
- Bind python requirement to version less than 4.0.0

### 🚜 Refactor

- Rename client to facade
- Make sshkeys and users modules public
- Change sshkeys list function to get_all
- Split pricing model into separate module
- Import PricingModel class directly in teams.py
- Move PricingModel to plans module
- Make sshkeys use base classes
- Add base classes to user classes
- Make teams classes use base resource classes
- Add base classes to server module
- Make regions module use base classes
- Make projects module use base classes
- Make plans module use base classes
- Make plan model fields nullable
- Make ip module use base classes
- Make image module use base classes
- Make block_storages use base classes
- Make backup storages use base classes
- Abstract _deployed module into for more general use
- Make server methods use get_model_copy()
- Make backup storages use conditional resource wait
- Remove deployable functionality from _backoff
- Remove unused _models module
- Rename _backoff module to _resource_wait
- Replace times sleeps with backoff polling
- Don't deep copy model, it's frozen
- Change all list getter name to list_by
- Change package name
- Rename user_agent_suffix to prefix in facade and _get_headers
- Rename _resource_wait to mor appropriate _resource_polling

### 📚 Documentation

- Add sphinx docs
- Update ssh key example
- Add user client examples
- Add AttachedServerModel to api docs
- Add facade example
- Fix server example
- Add additiona configuration link to block storage
- Update examples
- Remove hostname as identifier from server docs
- Split module autdocs into classes and fix some typos
- Correct facade init indent
- Add read the docs configuration file
- Rearrange docs conf.py import order
- Configure read the docs to work with poetry
- Add changelog url to pyproject.toml
- Add pre-commit recommendation to readme
- Fix project urls to point to organization repos

### 🧪 Testing

- Add cherry api client unit tests
- Add regions module integration tests
- Add project integration tests
- Make team_id fixture package scope
- Add plans integration tests
- Add package scope vps and project fixtures
- Add ips integration tests
- Add images integration tests
- Add block storage integration tests
- Move some fixtures to conftest from specific tests
- Make client unit test use _base requests
- Don't assert that requests were called with header params in client unit tests
- Add user unit tests
- Add teams unit tests
- Add ssh key unit tests
- Make teams and users client tests use helpers
- Add test helpers
- Fix api client test timeout params
- Add server unit tests
- Add server unit tests
- Minor fixes for ssh keys unit tests
- Refactor teams unit tests
- Refactor users unit tests
- Remove redundant teams unit tests
- Remove unused helper modules
- Add unit test helpers
- Add region unit tests
- Replace JSON type annotation with dict[str, Any]
- Add project unit tests
- Add plan unit tests
- Add IP unit tests
- Add images unit tests
- Add block storage unit tests
- Add backup storage unit tests

### ⚙️ Miscellaneous Tasks

- Add pytest dependency to pre-commit config
- Fix some linter complaints
- Update dependencies
- Add linting github action
- Add unit test workflow
- Add codecov to unit test workflow
- Add dependabot
- Add codecov config file
- Add integration test workflow
- Don't upload dependabot branch coverage
- Add dev group dependency to test workflows
- Configure pyproject.toml for poetry 2.0
- Add publishing workflow
- Set version to 1.0.0
- Configure docs and testing for release
- Update dependencies
- Configure repo for moving to cherryservers organization

<!-- generated by git-cliff -->
