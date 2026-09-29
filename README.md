# Dockerized Flask DevOps Lab

A simple Flask application containerized with Docker and deployed on an Ubuntu Server virtual machine.

## Tech Stack

- Ubuntu Server 24.04 LTS
- Docker
- Python 3.12
- Flask
- Git
- VirtualBox
- SSH

## Application

The Flask application provides:

- `/` - Main application page
- `/health` - Health check endpoint

## Build

docker build -t devops-flask-app .

## Run

docker run -d --name devops-flask -p 5000:5000 devops-flask-app

## Verify

curl http://localhost:5000

curl http://localhost:5000/health

Expected health response:

{"status":"healthy"}

## Architecture

Windows Host → VirtualBox → Ubuntu Server → Docker → Flask Application

## Author

Joseph Nicolas
