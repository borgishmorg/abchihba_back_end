#!/bin/bash

docker-compose up --build -d
sleep 30s
docker exec api alembic upgrade head
