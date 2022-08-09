VENV = .ssvenv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
UVICORN = $(VENV)/bin/uvicorn
PYTEST = $(VENV)/bin/pytest

all: test

test: $(VENV)/bin/activate
	# $(PYTHON) -m spacy download en
	$(PYTEST) -s


$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt
	# https://stackoverflow.com/questions/66992585/how-does-one-use-pytorch-cuda-with-an-a100-gpu
	# $(PIP) install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html


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