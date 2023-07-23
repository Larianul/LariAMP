#! /bin/bash
pods=$(kubectl get pods -l app=mysql -o jsonpath="{.items[*].metadata.name}")
for pod in $pods
do
kubectl logs -f $pod 
done

