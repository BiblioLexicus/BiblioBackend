#!/bin/sh

echo Installing docker images....

docker search mariadb

docker search python:3.9

echo Starting containers....

docker run --name mariadb -e MYSQL_ROOT_PASSWORD=@1 -p 3306:3306 -d docker.io/library/mariadb

sudo mariadb < dbConfig/MtlBiblioDb_V1-5.sql

img_id=docker build -t BiBlioLexicus/BiblioBackend:1.0 .

docker run -p 8000:8000 img_id

exit


