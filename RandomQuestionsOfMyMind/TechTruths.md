## Asynchronism

###Message queues

Message queues receive, hold, and deliver messages. If an operation is too slow to perform inline, you can use a message queue with the following workflow:

    An application publishes a job to the queue, then notifies the user of job status
    A worker picks up the job from the queue, processes it, then signals the job is complete


The user is not blocked and the job is processed in the background. During this time, the client might optionally do a small amount of processing to make it seem like the task has completed. For example, if posting a tweet, the tweet could be instantly posted to your timeline, but it could take some time before your tweet is actually delivered to all of your followers.

    Redis is useful as a simple message broker but messages can be lost.

    RabbitMQ is popular but requires you to adapt to the 'AMQP' protocol and manage your own nodes.

    Amazon SQS is hosted but can have high latency and has the possibility of messages being delivered twice.
    
###Task queues

Tasks queues receive tasks and their related data, runs them, then delivers their results. They can support scheduling and can be used to run computationally-intensive jobs in the background.

Celery has support for scheduling and primarily has python support.

## What is the difference between a message queue and a task queue? Why would a task queue require a message broker like RabbitMQ, Redis, Celery, or IronMQ to function?
    To put it simply: Task or message, they can be thought of or used interchangeably.  It's the asynchronous operation that matters. (repeat that last line to yourself :)) The point of having a queue is that one guy can ask to do something or say something and forget about it, and another guy can follow up on it.
    A task/message queue: Think of this like a passive data structure which acts like a queue, it 'stores' tasks and keeps them for processing later on. True, there is a process who manages this queue, but it doesn't do more, it just stores things and gives them when asked in an orderly way.
    Righto, great. But who processes it? The worker threads.
    Okay. So now, we have got 3 things.

    A task/message.

    A process who adds the tasks in to the task queue (data structure), and maintains this task queue.
    Worker processes who take the tasks/messages from this queue and execute them.
    So you mean workers can read this queue and remove tasks from them? Yes they can, but this leads to problems (er.. race conditions and such).

    Enter the 'message broker'.

    The 'message broker' is the one who takes the tasks from the task queue and distributes them to worker processes (even if they are on different machines) and manages the integrity of task completion, retrying tasks if workers fail, giving faster workers more tasks, and some other housekeeping for distributed processing.
    Aha! So that's what the message broker does!  Wait, why can't the 'Task/Message queue' manage the giving away of tasks to these workers, instead of just managing the queue?
    They can and do so, this is why there is confusion sometimes. Redis, primarily, a high performance passive data store,  also does message broking/scheduling
    Some message brokers (like rabbitMQ) use their own task queues to store and schedule them.
    
    The roles/functions may overlap, but the concept is essentially the same. 
    
### Another 
    Task Queue and Message Queue. RabbitMQ is a "MQ". It receives messages and delivers messages.

    Celery is a Task Queue. It receives tasks with their related data, runs them and delivers the results.

    Let's forget Celery for a moment. Let's talk about RabbitMQ. What would we usually do? Our Django/Flask app would send a message to a queue. We will have some workers running which will be waiting for new messages in certain queues. When a new message arrives, it starts working and processes the tasks.
    Celery manages this entire process beautifully. We no longer need to learn or worry about the details of AMQP or RabbitMQ. We can use Redis or even a database (MySQL for example) as a message broker. Celery allows us to define "Tasks" with our worker codes. When we need to do something in the background (or even foreground), we can just call this task (for instant execution) or schedule this task for delayed processing. Celery would handle the message passing and running the tasks. It would launch workers which would know how to run your defined tasks and store the results. So you can later query the task result or even task progress when needed.
    You can use Celery as an alternative for cron job too (though I don't really like it)!
    
    
### Final Words

    Celery is a queue Wrapper/Framework which takes away the complexity of having to manage the underlying AMQP mechanisms/architecture that come with operating RabbitMQ directly