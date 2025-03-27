#!/bin/bash
docker pull 515966524744.dkr.ecr.ap-northeast-2.amazonaws.com/jm-story-be:latest
docker run -d --name jm-story-be -p 8000:8000 515966524744.dkr.ecr.ap-northeast-2.amazonaws.com/jm-story-be:latest
