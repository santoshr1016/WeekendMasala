# WeekendMasala ¯\_(ツ)_/¯
    Writing code for fun!!!



## Eternally Thankful to Jodi Glickman for these words
### GIFT model

    
    generosity, 
    initiative, 
    forward momentum, and 
    transparency—to get ahead in your career.
    
    Most people don't love their job. It's this elusive goal that so many of us are chasing, and we never find, 
    looking for that dream job that you love. But we're barking up the wrong tree. 
    You shouldn't spend all of your time trying to find a job you love. Instead, 
    you should try and make people love you at work, every day, in every situation. 
    Because if I love you, I will do anything and everything in my power to help you succeed. 
    I will mentor you, I will sponsor you, I will champion your cause, I will give you great assignments, 
    I will pay you well, I will promote you, and you will love your job. 
    
    Here's the thing, if you love your job, you'll be better at it, and if you're better at your job, 
    then you'll like it more. It's a virtuous cycle, like your job more, be better at it. 
    Be better at your job, people like you or love you more.
 

### AWS HA


## Designing for failure

A quick overview of the high availability tools within AWS. Before we get started let's recap the AWS global infrastructure. 

    At the highest level AWS subdivides the world into regions. 

    Regions are geographically separated and located on almost every continent in the world. For example ap-south-1 is located in Mumbai, India. us-west-2, located in Oregon is in the United States. 

    Each region contains at least two availability zones or AZ's. 
    Each AZ is made up of at least one completely independent data center, connected through low-latency high-speed network links. 

    Independent of region or availability zone AWS also has edge location throughout the world. Located in placed like Chennai, India; Warsaw, Poland; Rio de Janeiro, Brazil; and South Bend, Indiana. These edge locations power CloudFront, the AWS content delivery network. The combination of edge locations, availability zones, and regions represent the AWS global infrastructure. 


Let's start the tour of high availability tools at the highest, most abstract level. 
Here we are looking at four completely isolated AWS regions. 

    The first stop on the tour of HA tools is Route 53. Route 53 is a service offering from AWS for managing domain name system or DNS requests. If you have the need to create and HA system that can tolerate the failure of an AWS region Route 53 is an important tool to have in your toolbox. Keep in mind that a failure of this magnitude is quite unlikely given all the redundency built into a given region. As with all component of your HA design you will want to balance the likelihood of failure, solution cost, and availability requirements. 

    The next stop on the HA tour finds us with in AWS region. Suppose you are running your application out of a single availability zone. If there was a catastrophic failure which took that AZ offline you would definitely be having a bad day. Enter the elastic load balance or ELB. ELB's represent one of the most foundational components of any HA solution within AWS. With the right application design and ELB configuration you can distribute your application components across additional AZ's and use an ELB to distribute traffic. 

    Suppose you have to operate a purchased application that only runs on a monolithic server. As such it can only exist in a single AZ on a single elastic compute cloud or EC2 instance. If there is a problem with that instance your application goes down and your users are disserviced. Another tool in the HA toolkit is the elastic IP address or EIP. An EIP can be reassigned from one instance to another. Instead of mapping your users directly to the IP of an EC2 instance you can map to the elastic IP. In the event of a failure you could create a new instance based off your most recent EC2 snapshot or backup. Then you can simply attach the EIP to the new instance. However, to guard against AZ failure you should consider bring that new instance up in a separate AZ. 

    So far we've talked about bad things happening. However, what if something good happens? Suppose you've designed you application and infrastructure to be running across three AZ's. All of a sudden you see an increase in load on your application. You can use a tool called an auto scaling group or an ASG to react to this load. Based on load figures you configure an ASG can launch additional instances to handle the increased demand. With an understanding of some of the abstract tools available let's look a little deeper into the additional service offerings that make them work. 


### Understanding fault tolerant components
It's possible to create remarkably fault tolerant and highly available applications using AWS. Let's look at some of the fundamental components you can use to design a robust, resilient system. 

    Let's start off by looking at data storage options. 
    Possibly the most well-known AWS storage offering is Simple Storage Service, or S3. It is the object storage offering that helped put AWS on the map. Accessible from anywhere there is an internet connection, it is a core component to have in your toolkit. 

    The next storage offering to be aware of is called Elastic Block Store, or EBS. EBS is storage which is directly attached to an elastic compute cloud, or an EC2, instance. Think of EBS as adding an additional hard drive to a single computer. 

    A more recent offering in the storage space is Elastic File System, or EFS. EFS can be configured so that thousands of EC2 instances can concurrently access the same mounted file system. You will see how you can use these storage components together to build resilient storage for your applications. 

### Now, let's take a look at database options. 

    If you have the luxury to build an application from scratch, 
    it's a great idea to look into DynamoDB. It is a non-relational, or no-sql database that has high availability baked into its design.
    
    If you operate an application that uses a relational database, AWS offers Relational Database Service, or RDS. Supporting both open-source and proprietary relational databases alike, RDS can be tailored to meet your recovery time and recovery point objectives. 
    
    For in memory data, AWS offers ElastiCache. With offerings that are compatible with Redis and Memcached, ElastiCache can be configured to run on a single node, or in a multi-availability zone cluster. 
    
    Now, let's explore some compute and networking components you're going to want to be familiar with, as you build out highly available applications. First, there is the Amazon Machine Image, or AMI. An AMI is an image from which a virtual machine can be launched. AMIs are particularly important in the context of high availability. 
    
    Suppose you need to quickly scale an application in order to deal with an increase in load. If you do, AMIs are an essential component for using Auto Scaling. Auto Scaling is a way to scale EC2 capacity up and down, based on triggers you define. For example, you can configure Auto Scaling to spawn additional copies of an EC2 instance if the CPU on a running instance exceeds 80 percent for two consecutive five minute periods. Of course, the triggering thresholds and durations are completely configurable to your needs. 
    
    Lambda is a completely event-driven way for you to run code without operating your own EC2 instances. Since the code within Lambda executes based on the occurrence of an event, Lambda can scale automatically. The Lambda paradigm forces you to adopt an atomic, stateless, microservice approach to software development. If you develop APIs, the API Gateway is an AWS offering that facilitates management of API performance, regardless of the scale required. The API Gateway integrates with Lambda, letting you focus on API development, while having the confidence that AWS is providing the infrastructure in a highly available fashion. 
    
    Other important high availability concepts include monitoring, alerting, and asynchronous messaging. To assist you on the monitoring front, AWS offers a service called CloudWatch. You can configure CloudWatch to monitor a variety of AWS-specific metrics. You can even custom configure metrics, and feed them to CloudWatch for monitoring and alerting. A common custom metric is EC2 instance memory. Since AWS operates at the hypervisor layer, that has no visibility into instance internals. You could operate your own queuing cluster within AWS using a product like RabbitMQ. If you go that route, you have to maintain the cluster yourself. AWS offers its own polling-based queuing product called Simple Queue Service, or SQS. Designed to be a highly available component, you can focus on using queues, instead of running things yourself. Since it is polling-based, queue subscribers can be offline, and messages will simply queue up. When the subscriber comes back online, the messages will process. Simple Notification Service, or SNS, is a highly available push-based messaging system. While SNS lacks the guaranteed delivery of SQS, these two components integrate very well. You can always push an event via SNS to an SQS queue. Another component that is most useful in designing highly available systems is the Elastic IP address, or EIP. Simply put, an EIP is a publicly accessible IP address that can be attached to an EC2 instance. If there is an issue with that instance, the EIP can simply be reassigned to a new one. While it's important to understand these components in isolation, it is only through automated integration that you truly appreciate their combined power. 


### AWS Load Balancing

    AWS provides load balancers as a service. These components let you design fault-tolerant highly available systems by distributing incoming traffic to more than one EC2 instance. 

Let's start off by reviewing how load balancing works. Suppose you have a web application residing on a single EC2 instance. If you route traffic to it directly, all user requests are being serviced by that single instance. If that instance fails, your users are having a bad experience. In order to reduce the risk of customer dissatisfaction, you'd love to be able to run three web servers and have them all handle traffic from your users. 
This is where an elastic load balancer or ELB comes into the picture. 
    It is a component that can split inbound traffic and distribute it to a variety of backend servers. What happens if you get many, many more users than you currently have and need to add additional servers to handle the load? Not to worry, the elastic in elastic load balancer means that the ELB scales automatically to handle the additional traffic. 

Let's talk about some important ELB features. First off, an ELB is a highly available component. That is, you don't have to stand up a standby ELB to point to a set of instances behind an existing ELB. However, it is possible for ELBs to fail. You can design around that by using Route 53 health checks on the ELB. If Route 53 detects an ELB failure, it can shift traffic to a different load balancer. 

    You can configure an ELB to be internal- or external-facing. 
    An internal ELB is useful if you want to increase the fault tolerance of internal application servers. 
    With an external ELB, you can accomplish the same objectives for internet-facing EC2 instances. 
    If you want to offload SSL/TLS processing from your EC2 instances, you can choose to terminate SSL/TLS on the ELB. 
    Another notable feature is the easy integration with AWS certificate manager. Certificate manager allows you to automate the deployment and renewal process for SSL/TLS certificates. 
    Similarly, ELBs integrate with AWS IAM. So you can define and assign security groups for granular networking controls. 
    You can create health checks on the ELB to monitor the state of an EC2 instance. If your health check fails, the instance is considered unhealthy and is removed from the load balancer.
    ELBs also support sticky sessions. Handled by load balancer-generated cookies, sticky sessions are great if your application needs to maintain state between a client and the EC2 instance that initially serviced the client's request. 

AWS offers a couple of different load balancing options. The original load balancing solution is called, the Classic Load Balancer. 
    
    One of its defining features is the ability to support both Layer 4 and Layer 7 load balancing. 
    Transport or Layer 4 load balancing is great if you need to load balance based on TCP. 
    Application or Layer 7 is useful when you have load balancing needs at the HTTP Layer. 
    
    Classic Load Balancer supports X-forwarded headers, as well as cookie-based sticky sessions. The Application Load Balancer or ALB is the newer of the AWS load balancing offerings. Despite the fact that it does not support transport layer load balancing, it does have some compelling features which make it very attractive to application developers. It has some capabilities which are not found in the Classic Load Balancer. 
    First off, it supports HTTP/2, an updated version of the venerable Hypertext Transfer Protocol. 
    HTTP/2 allows multiple requests to be sent on a single connection. 
    If you want to support multiple different services behind a single load balancer, you're in luck. 
    The ALB supports content-based routing to what AWS calls, target groups. A target group is simply a group of EC2 instances. Because of this, the ALB allows for health checks on a per port basis. 
    ALBs also support websockets which allow real-time two-way messaging over a long-running TCP connection. 
    Perhaps one of the most important features of the ALB is that it can support containerized applications. If you have a number of containers running on an EC2 instance, or are using the EC2 container service from AWS, you can use an ALB for load balancing. 
    
    
## Hiroshi Mikitani 10 Principles of Success

    1. All concepts are relative.
    Never believe in the absolute. No one single way of thinking is perfect.

    2. Believe in the power of the moonshot.
    Aim higher than you think is reasonably possible. It’s the stretch goal that fuels greatness.

    3. Learn the difference between a group and a team.
    A group is a gathering. A team is united towards a common goal. Don’t just do your job. 
    Think of yourself as part of the larger whole of the company – part of a team. 
    Success comes when you are part of an outstanding team.

    4. Think about your mindset, skills, and knowledge.
    Having the right attitude, the necessary skills and the desire to keep learning are the three key components to 
    personal success. If you’ve only got one or two, you may stall.
    
    5. Question yourself.
    Particularly when things are going well, question yourself and your process. What can you improve? Just because a process worked for you once before does not mean you don’t need to change and adapt going forward.

    6. A brand is a flag.
    When you run a company, you are doing more than just making money. You are assuming a role of leadership. Your brand is a symbol of your values, as important a symbol as a nation’s flag.

    7. The internet transformation continues.
    Fueled by the transformative powers of the internet, business will challenge national and government hegemony. Business creativity—the economic activity generated by the actions of everyone alive on the earth today—will create the new order.

    8. The internet will curate the world’s knowledge and data, but the human touch will still be key.
    No matter how far technology advances, people will be attracted to services that have a human touch. Tapping into human desires will be crucial to the continued success of the internet businesses. We tend to forget this because of our focus on rapidly advancing technology. But it’s precisely because we live in such a technological age that you can’t stand out or beat the competition with technology alone.

    9. Taking action leads to deeper thinking.
    If you are only taking action after thinking, you are on the wrong track. You should be taking action in order to think things through. That’s the right perspective.

    10. Continuously improve by a fraction. It’s the key to what others call “good luck.”
    If you improve by just 0.1 percent per day, after a year you will be 44 percent better at what you do. A little effort, every day, can make a big difference.