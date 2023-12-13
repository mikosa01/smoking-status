NAME=smoking-status
COMMIT_ID=$(shell git rev-parse HEAD)

build-ml-api-heroku:
	docker build --build-arg PIP_EXTRA_INDEX_URL=${PIP_EXTRA_INDEX_URL} -t registry.heroku.com/$(HEROKU_APP_NAME)/web:$(COMMIT_ID) .
	docker push registry.heroku.com/$(HEROKU_APP_NAME)/web:$(COMMIT_ID)
	heroku container:login
	heroku container:release web --app $(HEROKU_APP_NAME)
