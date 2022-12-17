# portfolio_site_py
Portfolio site written using Python and Django framework

### Useful command
#### Start docker
```docker-compose up -d --build```
#### Stop docker
```docker-compose down```
#### Collectstatic
```docker exec portfolio_site_web /bin/sh -c "python manage.py collectstatic --noinput"```
#### List all docker images
```docker images```
#### Delete <none> docker - docker is not being used
```docker rmi $(docker images --filter "dangling=true" -q --no-trunc)```