# Downlaod python dependencies, and create swagger.json file
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7-2020-06-06 as create-json

WORKDIR /app
COPY requirements.txt .

RUN \
    apt-get update && \
    apt-get install python3-psycopg2 -y && \
    apt-get install gcc -y && \
    pip install -r requirements.txt --no-cache-dir

ENV BUILD=building

COPY . /app

RUN python create_openapi.py

# Create SDK from swagger.json
FROM openapitools/openapi-generator-cli:v5.2.1 as build-sdk

COPY --from=create-json /app/openapi.json .

    # -g=javascript \
RUN ./usr/local/bin/docker-entrypoint.sh generate \
    -i=openapi.json \
    -g=typescript-axios \
    -o=/sdk \
    --additional-properties npmName={{cookiecutter.app_name}}_sdk \
    --skip-validate-spec

# Pack SDK to a tar file
FROM node:12-alpine as pack

WORKDIR /sdk

COPY --from=build-sdk /sdk .
COPY publish.sh /publish/
COPY --from=create-json /app/openapi.json /publish/

ENV _NPM_KEY="ENTER YOUR NPM KEY HERE"

RUN echo ${_NPM_KEY} >> /root/.npmrc &&\
      node --eval='const package=require("./package.json");package.name="@paraboly/"+package.name+"_sdk";console.log(JSON.stringify(package));' \
        >> temp.json &&\
      mv temp.json package.json

RUN npm install \
  && cp /publish/* . \
  && npm run-script build \
  && /bin/sh publish.sh \
  && npm pack

# Run the server
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7-2020-06-06

COPY . /app
COPY --from=create-json /usr/local/lib /usr/local/lib
COPY --from=pack /sdk/ /sdk

ENV TIMEOUT=600