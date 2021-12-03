#!/bin/bash
git pull
docker-compose -f production.yml up --build --force-recreate
