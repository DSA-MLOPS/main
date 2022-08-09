VENV = .ssvenv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
PYTEST = $(VENV)/bin/pytest
STREAMLIT = $(VENV)/bin/streamlit

srun: $(VENV)/bin/activate
	$(STREAMLIT) run app.py --server.runOnSave=true --server.enableCORS=false --server.enableXsrfProtection=false --server.port=8890


test: $(VENV)/bin/activate
	$(PYTHON) search.py
	

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

clean:
	rm -rf __pycache__
	rm -rf $(VENV)


# import deploy config
# You can change the default deploy config with `make cnf="deploy_special.env" release`
dpl ?= deploy.env
include $(dpl)
export $(shell sed 's/=.*//' $(dpl))

# grep the version from the mix file
VERSION=$(shell ./version.sh)


# HELP
# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help


# DOCKER TASKS
# Build the container
build: ## Build the container
	docker build -t $(HUB_USER)/$(REPO_NAME) .

build-nc: ## Build the container without caching
	docker build --no-cache -t $(HUB_USER)/$(REPO_NAME) .

run: ## Run container on port configured in `config.env`
	docker run -i -t --rm --env-file=./config.env -p=$(PORT):$(PORT) --name="$(REPO_NAME)" $(HUB_USER)/$(REPO_NAME)


up: build run ## Run container on port configured in `config.env` (Alias to run)

stop: ## Stop and remove a running container
	docker stop $(HUB_USER)/$(REPO_NAME); docker rm $(HUB_USER)/$(REPO_NAME)

push:
	docker push $(HUB_USER)/$(REPO_NAME)