#! /bin/bash

minikube delete

docker build -t apacheimg1 .

docker tag apacheimg1:latest larian147/apacheimg1:v1

docker login

docker push larian147/apacheimg1:v1

minikube start && minikube addons enable metrics-server	

kubectl create -f configmap.yaml

kubectl create -f deployment.yaml

kubectl create -f service.yaml

