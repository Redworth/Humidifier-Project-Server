# Redworth Humidifier IoT Project - IoT Backend Application

[![Redworth](https://img.shields.io/circleci/build/github/Redworth/Humidifier-Project-Server/master?label=circleci&logo=circleci&token=11612bf0a41cefd234dd928bd1bb20922a3bb5f6)](https://app.circleci.com/pipelines/github/Redworth/Humidifier-Project-Server?branch=master)
[![Build and Deploy to AKS Dev Cluster](https://github.com/Redworth/Humidifier-Project-Server/actions/workflows/azure_kubernetes_service_workflow.yml/badge.svg)](https://github.com/Redworth/Humidifier-Project-Server/actions/workflows/azure_kubernetes_service_workflow.yml)

This git repository contains the code for our IoT backend for the IoT Humidifier project.

## Environment Setup
Prerequisites:
- Python 3 (any version) and pip3 installed
- Git installed
- Any editor that supports Python development
- Docker installed

Clone the git repository (https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository). Then create a feature branch (https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) to work on the code.

Run `pip3 install -r requirements.txt` to install the needed dependencies.

The environment is now ready for development.

## Usage
Prerequisites:
- Environment is setup (see above)

For everyday usage, running directly with Python is sufficient. Run `python3 main.py` or `export FLASK_APP="main.py" && flask run` to begin the flask development server. Any edits to the code will then be live reloaded.

To build and run locally with Docker, execute:
```
docker build -t humidifier-project-server .
docker run -d -p 8000:8000 humidifier-project-server
```

To execute a package pulled from Github Packages:
`docker run -d -p 8000:8000 ghcr.io/redworth/humidifier-project-server:latest`

## Downloading and Uploading Packages
To push/pull to the container registry, a Github personal access token is required.

Download the latest image from Github Packages using the following commands:
```
docker login ghcr.io --username <github-username> --password <github-pat>
docker pull ghcr.io/redworth/humidifier-project-server:latest
```

To build and publish images to Github Packages:

```
docker login ghcr.io --username <github-username> --password <github-pat>
docker build -t ghcr.io/redworth/humidifier-project-server:latest .
docker push ghcr.io/redworth/humidifier-project-server:latest`
```

To build and publish to a different registry, substitute `ghcr.io` for a different registry domain.