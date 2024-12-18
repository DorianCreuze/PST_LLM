@echo off
REM Run Docker container with GPUs and mount volume
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

REM Execute a command in the running Docker container
docker exec -it ollama ollama pull llama3.1:8b

REM Create a Docker network
docker network create ollama-network

REM Connect the running container to the network
docker network connect ollama-network ollama

REM Build a Docker image for Python summarizer
docker build -t python-summarizer .

REM Run the Flask application container connected to the network
docker run -d --name flask-app --network ollama-network -p 5000:5000 python-summarizer
