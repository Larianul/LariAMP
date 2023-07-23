#! /bin/bash

kubectl exec  -it apache-86b85cc47d-tdpln -- apt-get install htop -y && apt-get update


kubectl exec  -it apache-86b85cc47d-tdpln -- htop 
