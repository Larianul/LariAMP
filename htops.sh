#! /bin/bash
pods=$(kubectl get pods -l app=apache -o jsonpath="{.items[*].metadata.name}")
for pod in $pods
do
kubectl exec  -it $pod -- apt-get install htop -y && apt-get update


kubectl exec  -it $pod -- htop 

done

