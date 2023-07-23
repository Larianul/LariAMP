#! /bin/bash

kubectl exec  -it mysql -- apt-get install htop -y && apt-get update


kubectl exec  -it mysql -- htop 


