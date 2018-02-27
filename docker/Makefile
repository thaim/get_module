IMAGE=thaim/get_module
VERSION=$(shell echo `cat VERSION`)

.PHONY: help build push

help: ## show this help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {sub("\\\\n",sprintf("\n%22c"," "), $$2);printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

build: ## build docker image
	cp ../get_modules.py .
	docker build \
		-t $(IMAGE):latest \
		-t $(IMAGE):$(VERSION) \
		.

push: ## push docker image to docker hub
	docker push $(IMAGE):latest
	docker push $(IMAGE):$(VERSION)
