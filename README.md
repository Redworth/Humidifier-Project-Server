# Redworth Humidifier IoT Project - IoT Backend Server Application

[![Build Status](https://dev.azure.com/Redworth-Projects/Humidifier%20Development/_apis/build/status/Humidifier-Development-Build?branchName=master)](https://dev.azure.com/Redworth-Projects/Humidifier%20Development/_build/latest?definitionId=3&branchName=master)

This git repository contains the code for our IoT backend for the IoT Humidifier project.

## Usage
This backend code uses docker to build and run. To build and run locally, execute:
```
docker build -t humidifier-project-server .
docker run -d -p 8000:8000 humidifier-project-server
```

To build so images can be pushed to Github Packages:
`docker build -t ghcr.io/redworth/humidifier-project-server:latest .`

To execute a package pulled from Github Packages:
`docker run -d -p 8000:8000 ghcr.io/redworth/humidifier-project-server:latest`

## Installation
To push/pull to the container registry, you must have a Github personal access token.

Download the latest image from Github Packages using the following commands:
```
docker login ghcr.io --username <github-username> --password <github-pat>
docker pull ghcr.io/redworth/humidifier-project-server:latest
```

## Uploading Packages
To upload images to Github Packages:

```
docker login ghcr.io --username <github-username> --password <github-pat>
docker push ghcr.io/redworth/humidifier-project-server:latest`
```

## Contribute
Users with access to this git repository can contribute by creating a pull request. The team can discuss and review the code after that.
