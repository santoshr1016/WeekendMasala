## What is a Secrets Engine?
Vault provide a REST api kind a interface to communicate with it.  A secrets engine is enabled at a path. 
Vault itself performs prefix routing on incoming requests and routes the request to the correct secrets engine based on the path at which they were enabled.

By default, Vault enables a secrets engine called kv at the path secret/. The kv secrets engine reads and writes raw data to the backend storage.
There are other secret engines like AWS, MySQL, Google cloud, K8S, LDAP

## Enable and Perform CRUD operation to a Secret Engine
```bash
# A KV secret engine and enabling it
$ vault secrets enable -path=kv kv
Success! Enabled the kv secrets engine at: kv/
    
$ vault secrets list
Path          Type         Accessor              Description
----          ----         --------              -----------
cubbyhole/    cubbyhole    cubbyhole_76596432    per-token private secret storage
identity/     identity     identity_8942b862     identity store
kv/           kv           kv_9de40d33           n/a
secret/       kv           kv_0dc2c8e6           key/value secret storage
sys/          system       system_487422bd       system endpoints used for control, policy and debugging
   
## Writing the secrets
       
$ vault write kv/hello target=world
Success! Data written to: kv/hello
    
$ vault write kv/airplane type=boeing class=787
Success! Data written to: kv/airplane 

    
$ vault write secret/my-secret value=mypassword
Success! Data written to: secret/my-secret
        
## Reading the secrets
    
$ vault read kv/hello
Key                 Value
---                 -----
refresh_interval    768h
target              world

    
$ vault read secret/my-secret
Key                 Value
---                 -----
refresh_interval    768h
value               mypassword
    
## Delete a secret
    
$ vault delete  secret/my-secret
Success! Data deleted (if it existed) at: secret/my-secret

```
 