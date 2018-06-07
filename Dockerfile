FROM alpine:latest

RUN apk add --no-cache --update python3 python3-dev py3-pip supervisor build-base linux-headers && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    pip3 install uwsgi django PyYAML markdown && \
    rm -r /root/.cache && \
    apk del build-base linux-headers

EXPOSE 8000
COPY app /app/
COPY config /etc/app/
WORKDIR /app/
CMD ["supervisord", "-n", "-c", "/etc/app/supervisor.conf"]

