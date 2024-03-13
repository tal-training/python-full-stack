Here's a step-by-step guide for beginners on how to install Docker on an EC2 Linux instance and run a container from Docker Hub
Step 1: Launch an EC2 Instance

1. Go to the AWS Management Console and navigate to the EC2 dashboard.
2. Click on "Launch Instance" in the top right corner of the page.
3. Select "Linux" as the operating system and choose your preferred Amazon Machine Image (AMI).
4. Choose the instance type and configure the other settings as desired.
5. Make sure to select the appropriate security group that allows traffic on ports 22 (SSH) and 80 (HTTP).
6. Click "Launch" to launch the instance.

Step 2: Install Docker

1. Connect to your EC2 instance using SSH. You can use a tool like PuTTY or the built-in SSH client in the AWS Management Console.
2. Update the package list and install Docker using the following command:
```
sudo yum update -y
sudo yum install docker.io -y
```
3. Start the Docker service and enable it to start automatically at boot time:
```
sudo systemctl start docker
sudo systemctl enable docker
```

Step 3: Pull a Container Image from Docker Hub

1. Use the Docker CLI to pull a container image from Docker Hub. For example, to pull the latest version of the nginx image, use the following command:
```
docker pull nginx
```
2. Verify that the image was pulled successfully by listing the images with the `docker images` command:
```
docker images
```

Step 4: Expose Ports with the `-p` Flag

1. To expose a port on the host machine, you can use the `-p` flag when running a container. For example, to expose port 80 on the host machine and map it to port 80 inside the container, use the following command:
```
docker run -d -p 80:80 nginx
```
This will start a new container named "nginx" based on the nginx image and map port 80 on the host machine to port 80 inside the container. The `-d` flag runs the container in detached mode, which means it runs in the background and does not interactively prompt the user.

2. Verify that the container is running correctly by listing the containers with the `docker ps` command:
```
docker ps
```
You should see the container ID, image name, and status for the container you just created.
3. Access the container's web server by using the public IP address or DNS name of your EC2 instance followed by the port number that the container is listening on. In this case, you can access the container's web server by navigating to <http://ec2-public-ip-address:80>. Replace "ec2-public-ip-address" with the actual public IP address or DNS name of your EC2 instance.

That's it! You have now successfully exposed a port on your EC2 instance using the `-p` flag and accessed the container's web server from outside the container.