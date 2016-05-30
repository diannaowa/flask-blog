FROM ubuntu:14.04
MAINTAINER walter.liu@yeahmobi.com

RUN mkdir -p /data && mkdir /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY ./flask-blog /data/
WORKDIR /data/
RUN apt-get update && apt-get install -y libmysqlclient-dev && \
    apt-get install -y python-dev supervisor python-pip && pip install -r requirements.txt && \
    python manage.py db init && python manage.py db migrate && python manage.py db upgrade && \
    apt-get clean all
EXPOSE 80
CMD ["/usr/bin/supervisord"]
