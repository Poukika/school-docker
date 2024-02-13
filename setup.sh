#!/bin/bash

docker image build ./authentication -t authen_exam_docker:latest
docker image build ./authorization -t autho_exam_docker:latest
docker image build ./content -t content_exam_docker:latest


if [[ -d './log_volume' ]]
then
    echo "/log_volume already exists"
else
    mkdir log_volume
fi

docker-compose up fastapi -d
docker-compose up
docker-compose down 
