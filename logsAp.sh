#! /bin/bash
pods=$(kubectl get pods -l app=apache -o jsonpath="{.items[*].metadata.name}")
for pod in $pods
do
kubectl exec  $pod cat /var/log/apache2/access.log
done

