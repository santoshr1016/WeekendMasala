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
### Configuring the Notification 