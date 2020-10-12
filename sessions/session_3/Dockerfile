FROM python:3.8.6-alpine

COPY . session3/.

WORKDIR /session3

# install make
RUN apk update \
    && apk add make

# run the init, lint and tests with make
RUN make

CMD ["python", "run.py"]