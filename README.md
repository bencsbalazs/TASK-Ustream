# Budapest Lab exercise

Balázs Bencs

> 

1. Create environment
    1. Install Rancher-desktop (as suggested)
    2. Install Docker
    3. Install Terraform
    4. Install Helm
    5. Install kubernetes

2. Create microservice structure
    1. Create Dockerfile
    2. Create app.py - It listening on two endpoints. On default, and metrics. The metrics is in openmetrics format, what can be process tthrough the endpoint.
    3. Add requirements.txt (test the application in a virtualenv)
    4. Create charts folder
    5. Add the charts/Chart.yaml
    6. Add values.yaml with the docker credentials 

3. Prepare for deployment
    1. Build the Docker image
    2. Push docker image to repository
    3. Create deployment.yaml
    4. Run this file with `kubectl apply -f deployment.yaml`
    5. Create service.yaml
    6. Run the file with `kubectl apply -f service.yaml`
    7. Create cronjob

4. View metrics
    1. Install prometheus server
    2. Access the endpoints from browser.