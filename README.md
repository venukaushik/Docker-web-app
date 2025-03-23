# Dockerized Python Flask Web Application

This repository contains a simple Python Flask web application that provides information about Docker. The application is containerized using Docker, making it easy to run and deploy in any environment that supports Docker.

## Table of Contents

* [Description](#description)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Cloning the Repository](#cloning-the-repository)
* [Running with Docker](#running-with-docker)
    * [Building the Docker Image](#building-the-docker-image)
    * [Running the Docker Container](#running-the-docker-container)
    * [Accessing the Application](#accessing-the-application)
* [Running Locally (Optional)](#running-locally-optional)
    * [Prerequisites](#prerequisites-local)
    * [Installation](#installation)
    * [Running the Application](#running-the-application-local)
* [Endpoints](#endpoints)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

## Description

This project is a Python Flask web application designed to provide notes and common commands related to Docker. It features multiple endpoints to offer information on different aspects of Docker, such as images, containers, and Dockerfile basics. The application itself is packaged within a Docker container for easy deployment and portability.

## Getting Started

### Prerequisites

* **Docker:** You need to have Docker installed on your system to run the containerized application. You can find installation instructions on the official Docker website: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
* **(Optional) Python 3 and pip:** If you want to run the application locally without Docker, you'll need Python 3 and pip installed.

### Cloning the Repository

First, clone this repository to your local machine using Git:

```bash
git clone https://github.com/venukaushik/Docker-web-app
cd Docker-web-app
