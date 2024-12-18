#!/bin/bash

docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
docker exec -it ollama ollama pull llama3.1:8b
docker network create ollama-network
docker network connect ollama-network ollama
docker build -t python-summarizer .
docker run -d --name flask-app --network ollama-network -p 5000:5000 python-summarizer