#!/bin/bash

ECR_IMAGE="515966524744.dkr.ecr.ap-northeast-2.amazonaws.com/jm-story-be:latest"
CONTAINER_NAME="fastapi-backend"

# 기존 컨테이너 정리
docker rm -f $CONTAINER_NAME || true

# 최신 이미지 가져오기
aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin 515966524744.dkr.ecr.ap-northeast-2.amazonaws.com/jm-story-be
docker pull $ECR_IMAGE

# 컨테이너 실행
docker run -d \
  --name $CONTAINER_NAME \
  -p 8000:8000 \
  $ECR_IMAGE