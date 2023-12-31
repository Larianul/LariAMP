## Creating a Docker Image

To create a Docker image for your application, follow these steps:

1. Create a Dockerfile in your project directory using a text editor or IDE.
2. Add the necessary commands to the Dockerfile to build your application.
3. Build the Docker image using the command `sudo docker build -t <image-name> .`, where `<image-name>` is the name you want to give your image.
4. Verify that the image was created correctly by running the command `sudo docker images`.
5. Push the Docker image to Docker Hub using the command `sudo docker push <docker-hub-username>/<image-name>:<tag>`.
6. Verify that the image was pushed correctly by logging in to Docker Hub and checking your repository.


## Creating Kubernetes Manifest Objects

To create Kubernetes manifest objects for your application, follow these steps:

1. Create a YAML file for the object you want to create (e.g. Deployment, Service, etc.) using a text editor or IDE.
2. Add the necessary fields to the YAML file to define your object.
3. Create the object using the command `kubectl apply -f <yaml-file>`, where `<yaml-file>` is the name of the YAML file you created.
4. Verify that the object was created correctly by running the command `kubectl get <object-type>`, where `<object-type>` is the type of object you created (e.g. Deployment, Service, etc.).

!! Consider modifying the path to the image in ApachePHP/deployment.yaml to the personal-created one
## Testing

To test the LoadBalancer service of the Kubernetes cluster, follow these steps:

1. Use the Python-based GUI to monitor system resources and traffic on each instance.
2. Set and reset nodes as needed using the included bash scripts.

