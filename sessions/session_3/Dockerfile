FROM python:3.8.6-alpine

COPY . session3/.

WORKDIR /session3

RUN pip install -r requirements.txt \
    && apk update \
    && apk add make

CMD ["make"]