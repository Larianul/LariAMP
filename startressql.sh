#! /bin/bash

if minikube status | grep -q "Running"; then
    echo "Minikube is running, not deleting it."
else
    minikube delete
fi

docker build -t mysqlimg ./MySql/

docker tag mysqlimg:latest larian147/mysqlimg:latest

docker login

docker push larian147/mysqlimg:latest

minikube start && minikube addons enable metrics-server	

kubectl apply -f MySql/configmap.yaml

kubectl apply -f MySql/deployment.yaml

kubectl apply -f MySql/service.yaml

