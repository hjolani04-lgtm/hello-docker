# Hello Docker

A small Python web server packaged with Docker.

## Build
docker build -t hello-docker:1.0 .

## Run
docker run -d --name hello -p 8000:8000 hello-docker:1.0
curl localhost:8000

## Override at runtime
- Environment variable: `-e APP_NAME="My Name"`
- Port argument: `docker run -d -p 9100:9500 hello-docker:1.0 9500`

## Dockerfile instructions used
FROM, LABEL, ARG, ENV, WORKDIR, COPY, RUN, USER, EXPOSE, ENTRYPOINT, CMD
