# dockertest

## Sources

- https://djangostars.com/blog/what-is-docker-and-how-to-use-it-with-python/ Python, Termonology, Nginx


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


## Good practices

- Include only necessary context — use a .dockerignore file (like .gitignore in git)
- Avoid installing unnecessary packages — it will consume extra disk space
- Use cache. Add context which changes a lot (for example source code of your project) at the end of Dockerfile — it will utilize Docker cache effectively.
- Be careful with volumes. You should remember what data is in volumes. Because volumes are persistent and don’t die with the containers - next container will use data from volume which was created by previous container.
- Use environment variables (in RUN, EXPOSE, VOLUME). It will make your Dockerfile more flexible.
- Docker compose — is the only right way to connect containers with each other.
