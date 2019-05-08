## This is opinionated guideline which I have followed, there can be multiple ways to achieve the same.
## This should help anyone who want to learn / build Jenkins Pipeline from Scratch.

# Step 1. Creating a Jenkins master
### 1. Setup Security group
### Purpose
#### They act as firewall to the instances.
#### They provide well identified / defined Ports for the incoming and outgoing traffic.
``` Python
Configuring the outbound traffic
Open to all

Configuring the inbound traffic
Set up the  SSH, HTTP, HTTPS type with proper source 
Tag the SG
Now the SG is ready and it can be attached to EC2 instance.
```
### 2. Setup Key pair
### Purpose
#### To ssh the EC2 instance where Jenkins master is running.
 
# Step 2 Make them live
```python
1. Create an ec2 instance now
2. Take ubuntu18.04 AMI LTS
3. Attach the SG that was created.Should be in same VPC
4. Attach the KeyPair
5. Create a Elastic IP and attach it to the instance
```
# Step 3
### Now we have got all the virtual hardware, We need to install the software now.
### We need to install Java RT(Jenkins is Java based) and Nginx(Reverse proxy)

```python
Get into the EC2 instance and install the packages

wget http://pkg.jenkins-ci.org/debian-stable/jenkins-ci.org.key

apt-key add jenkins-ci.org.key
echo "deb http://pkg.jenkins-ci.org/debian binary/" > /etc/apt/sources.list.d/jenkins.list
apt update
apt upgrade
apt install -y openjdk-8-jdk
apt install -y nginx
apt install jenkins -y

Check the process using the systemctl
systemctl status nginx | grep Active
systemctl status jenkins | grep Active

```
# Step 4 
### Configuring the Jenkins and Nginx
```python
We configure Nginx to act as reverse proxy that sits in front of Jenkins web application
All the traffic goes via Nginx, but whats the benifit we get.
```
### 1. Application Server security
```python
Jenkins listens on port 8080 by default. By setting up a security group and a reverse proxy that only allow access
on port 80 we can make sure that all requests to the app server come through the web server first. 
This gives the app server some protection by limiting access to it. We can also use some of NGINX's other security 
features like simple password protection or limiting access by IP address.
```

### 2. Logging 
```python
The reverse proxy also gives us the benefit of generating logs for each request. Jenkins does create logs but the 
content is more operational in terms of what Jenkins is doing, not what an end user is doing. By logging requests 
in the proxy, we get much more information like when and where requests are coming from. So if there's ever a need 
to debug an issue with a server, the NGINX logs will make a great compliment to the Jenkins logs.

```
### 3. SSL Termination
Using NGINX as a reverse proxy also allows for simplified SSL termination. With SSL, all the traffic from the 
Jenkins application would be encrypted. That improves the security of their information being transmitted. And 
while it's not impossible to set up SSL termination using Jenkins alone, setting up SSL in NGINX is much easier.

# Step 5
### Configuring the Notification using SES
```python
1. Create a valid email address to which jenkins notification will be sent
2. We also need to create SMTP credentials that Jenkins will use to connect to SES for sending email
3. Provide our Jenkins SMTP configuration, including the server name and the port numbers.

Put all this info in Jenkins -> Manage ->configure ->email 
```
# ******** Building the Actual CI/CD Pipeline ********
```textmate
So far, we already have a server running our Jenkins master. 
Before we create any more resources, let's plan the rest of the build environment. 
```

### Best Practice distributed Jenkins
```python
We will follow best practices for a distributed Jenkins environment by removing all executors from the Jenkins master. 
This will prevent any builds from starting on the master server. 
```
### Advantages of removing all Executors
```python
Not running builds on the master frees up resources for Jenkins to do what it does best, managing builds on other servers. 
```

### How to acheive 
```python
To connect our master server to build servers, we'll need to create a key pair for connections via Secure Shell and 
a security group to limit access to only the Jenkins master server, and of course, we'll need at least one build server. 

This is where the real action happens. 

Any code that gets checked out will be written to these servers and commands will be run by local processes. 
The results of the build will get sent back to the Jenkins master for any post-build processing like archiving or reporting. 
Because our build server will be manipulating AWS resources on our behalf, we need to create an IAM role that gives 
the correct permissions to the services we want to deploy. The role will allow our build servers to run AWS commands 
and interact with AWS APIs without having to enter credentials. 

As automators, this is an enormous benefit for us because we don't have to worry about storing and retrieving credentials 
every time we want the build server to do something. Once we have all of these resources in place, we'll be able to create Jenkins jobs 
that can deploy and manage resources like S3, EC2, and Elastic Beanstalk.

Our goal will be to set up a pipeline triggered by pushes to a GitHub repository so that codechanges are deployed automatically. 
Essentially, we'll be building the infrastructure for a continuous integration and continuous delivery pipeline, also known as CICD.
```