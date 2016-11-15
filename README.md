# flask-blog
A simple blog system, it can be managed locally docker

Please start mysql service or container on your host,then edit the config.py


start blog:
```shell
python manage.py db upgrade

python manage.py db migrate

python manage.py runserver --host=0.0.0.0 
```
start websocket
```shell
python webso/run.py
```

#Or
```shell
docker run -d --name blog -p 8080:80 duizhang/blog

http://HOST_IP:8080

http://HOST_IP:8080/post 
```
