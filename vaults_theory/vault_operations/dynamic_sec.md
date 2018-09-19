## Dynamic secrets
Dynamic secrets are generated when they are accessed, Unlike the kv secrets where you had to put data into the store yourself.
Dynamic secrets do not exist until they are read, so there is no risk of someone stealing them or another client using the same secrets. 
Because Vault has built-in revocation mechanisms, dynamic secrets can be revoked immediately after use, minimizing the amount of time the secret existed.


## AWS Dynamic Secret
To create AWS dynamic secret the process goes through different stages

#### Stage 1    Enable AWS secrets engine
```bash
$ vault secrets enable -path=aws aws
Success! Enabled the aws secrets engine at: aws/
    
#The AWS secrets engine is now enabled at aws/.
```

#### Stage 2    Configuring the AWS Secrets Engine 
After enabling the AWS secrets engine, you must configure it to authenticate and communicate with AWS. This requires privileged account credentials
```bash
$ vault write aws/config/root \
    access_key=AKIAI4SGLQPBX6CSENIQ \
    secret_key=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
Success! Data written to: aws/config/root
    
# These credentials are now stored in this AWS secrets engine. The engine will use these credentials when communicating with AWS in future requests.
```
#### Stage 3    Creating Role and attaching IAM Policy
```bash
$ vault write aws/roles/my-role policy=-<<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1426528957000",
      "Effect": "Allow",
      "Action": [
        "ec2:*"
      ],
      "Resource": [
        "*"
      ]
    }
  ]
}
EOF
Success! Data written to: aws/roles/my-role
    
# A named role "my-role" is created with an IAM Policy to attach with. 
```

#### Stage 4    Generating the Secret 
```bash
$ vault read aws/creds/my-role
Key                Value
---                -----
lease_id           aws/creds/my-role/0bce0782-32aa-25ec-f61d-c026ff22106e
lease_duration     768h
lease_renewable    true
access_key         AKIAJELUDIANQGRXCTZQ
secret_key         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
security_token     <nil>
```
The access and secret key can now be used to perform any EC2 operations within AWS. Notice that these keys are new, 
they are not the keys you entered earlier. If you were to run the command a second time, you would get a new access key pair. 
Each time you read from aws/creds/:name, Vault will connect to AWS and generate a new IAM user and key pair.

#### Stage 4    Revoking the Secret 

Vault will automatically revoke this credential after 768 hours (see lease_duration in the output), but perhaps we want to revoke it early. 
Once the secret is revoked, the access keys are no longer valid.
```bash
$ vault lease revoke aws/creds/my-role/0bce0782-32aa-25ec-f61d-c026ff22106
Success! Revoked lease: aws/creds/my-role/0bce0782-32aa-25ec-f61d-c026ff22106e
```
