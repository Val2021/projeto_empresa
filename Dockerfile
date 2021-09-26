FROM       ubuntu:18.04
MAINTAINER Docker

ARG DEBIAN_FRONTEND=noninteractive

# Installation:
RUN apt-get update && apt-get install -y python3 
RUN apt-get install -y python3-setuptools
RUN apt-get install -y python3-pip
RUN apt-get install -y nano
RUN apt-get install -y telnet
RUN apt-get install -y vim
RUN  apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip 

RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add -
RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list

# Update apt-get sources AND install MongoDB
RUN apt-get update && apt-get install -y mongodb-org

# Create the MongoDB data directory
RUN mkdir -p /data/db

# Create the MongoDB data directory
RUN mkdir -p /data/code

RUN pip3 install bottle

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt /usr/src/app
RUN pip3 install -r requirements.txt

# copy project
COPY . /usr/src/app

# Expose port #27017(mongoDB) and #8000(python server)
EXPOSE 27017
EXPOSE 8000

COPY runner.sh /scripts/runner.sh
RUN ["chmod", "+x", "/scripts/runner.sh"]
ENTRYPOINT ["/scripts/runner.sh"]
