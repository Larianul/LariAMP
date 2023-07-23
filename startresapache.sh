#! /bin/bash

if minikube status | grep -q "Running"; then
    echo "Minikube is running, not deleting it."
else
    minikube delete
fi

docker build -t apacheimg1 ./ApachePHP

docker tag apacheimg1:latest larian147/apacheimg1:v1

docker login

docker push larian147/apacheimg1:v1

minikube start && minikube addons enable metrics-server	

kubectl apply -f ApachePHP/configmap.yaml

kubectl apply -f ApachePHP/deployment.yaml

kubectl apply -f ApachePHP/service.yaml

