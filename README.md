# dockertest

## Basic dockersetup and terminal commands
- `docker build -t friendlyhello .` Requires some files. Creates docker image. `docker image ls`
- `docker run -p 4000:80 friendlyhello` Maps port 4000 locally to port 80 on docker. 
- `docker run -d -p 4000:80 friendlyhello` Run the docker in detached mode.


### Dockerhub

- `docker tag image_name username/repository:tag`
- `docker push username/repository:tag`

### docker_compose.yml

https://docs.docker.com/get-started/part3/#about-services

## Sources

- https://www.ybrikman.com/writing/2015/05/19/docker-osx-dev/ Rolig o bra förklaring om varför Docker är viktigt
- https://djangostars.com/blog/what-is-docker-and-how-to-use-it-with-python/ Python, Termonology, Nginx
- https://pipelines.puppet.com/docs/tutorials/build-and-deploy-python-with-docker/
- https://snarky.ca/what-are-the-popular-docker-images-for-python/ Which python image to use (Alpine? Eller Anaconda för data science)
- https://hub.docker.com/r/datmo/kaggle/ ML dockers. Fattar ej hur man ser builden
- https://medium.com/@evheniybystrov/docker-for-data-science-9c0ce73e8263 Docker for Data Science
- https://hackernoon.com/making-right-things-using-docker-7296cf0f6c6e Tillhör ovanstående
- https://docs.docker.com/compose/networking/#multi-host-networking docker compose. Networking dockers
- https://www.youtube.com/watch?v=Qw9zlE3t8Ko&t=69s docker compose **
- https://www.youtube.com/watch?v=sz96JV8S-Bk automate builds with git
- https://stackoverflow.com/questions/25552038/how-to-update-a-docker-image Udating images etc
- https://tsaprailis.com/2017/10/10/Docker-for-data-science-part-1-building-jupyter-container/ Jupyter within docker
- https://stackoverflow.com/questions/21553353/what-is-the-difference-between-cmd-and-entrypoint-in-a-dockerfile CMD vs ENTRYPOINT
- https://hub.docker.com/r/jupyter/datascience-notebook/ data science docker
- https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook lite om att utveckla med jupyter
- https://www.ctl.io/developers/blog/post/dockerfile-entrypoint-vs-cmd/ ENTRY vs CMD

## Goals

- Basic docker
- API docker
- Dockers communicating
- Database docker
- Kubernetes

## Dockerfile


### Commands
- `FROM` — set base image
- `RUN` — execute command in container
- `ENV` — set environment variable
- `WORKDIR` — set working directory
- `VOLUME` — create mount-point for a volume
- `CMD` — set executable for container


"There can be only one CMD command. It’s the philosophy of docker — one process per container."

## Good practices

### 1
- Include only necessary context — use a .dockerignore file (like .gitignore in git)
- Avoid installing unnecessary packages — it will consume extra disk space
- Use cache. Add context which changes a lot (for example source code of your project) at the end of Dockerfile — it will utilize Docker cache effectively.
- Be careful with volumes. You should remember what data is in volumes. Because volumes are persistent and don’t die with the containers - next container will use data from volume which was created by previous container.
- Use environment variables (in RUN, EXPOSE, VOLUME). It will make your Dockerfile more flexible.
### 2 Connect
- Docker compose — is the only right way to connect containers with each other.
### 3
- 1 application = 1 container
- Run process in foreground (don't use systemd, upstart or any other similar tools)
- Keep data out of container — use volumes
- Do not use SSH (if you need to step into container you can use docker exec command)
- Avoid manual configurations (or actions) inside container
