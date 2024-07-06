# Take Home - Django Skeleton

## Getting Started
Dependencies:
* Docker - See [Get Docker](https://docs.docker.com/get-docker/)
* Docker Compose - Installed with Docker Desktop, See [Install Docker Compose](https://docs.docker.com/compose/install/)

With the dependencies installed, running the project is as simple as running:
```bash
docker compose up
```

This will pull the required Docker images and spin up a container running your service on http://localhost:8000.

To end the service, press `Ctrl+C`

## Project
This Project is about Getting Weather information from the Third party API and give it in API.

## Description
* Here we have created api for getting the weather information and alerts like you can weather go out or not
* There is an API call '/check_weather' for getting that information. We simply have to pass the city parameter to get that information.
