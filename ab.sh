#! /bin/bash

kubectl exec  -it apache-69856fddf8-m6bxt -- apt-get install apache2-utils -y && apt-get update


kubectl exec  -it apache-69856fddf8-m6bxt -- ab -n 100 -c 10 http://192.168.49.2:31098/ 
