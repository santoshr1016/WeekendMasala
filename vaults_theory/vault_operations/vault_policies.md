## Vault Policies
Like an AWS IAM policies Vault policy instructs what specific actions are allowed to the paths / endpoints within the Vault.
These policies are associated with specific Secrets Backend.
So, when a user is authenticated against a backend, the policies attached that backend determines what action the user can perform.            
Policies are written in Hashicorp Config Language


## Writing a Vault Policy
    
#### Stage 1    Writing policy in HCL file
```hcl

path "secret/dev/*" {
  capabilities = ["read","create","update", "delete", "list"]
}


path "secret/test/*" {
  capabilities = ["read","create","update", "delete", "list"]
}

# save this policy to dev-team-policy.hcl
```

#### Stage 2    Upload and listing of policy
```bash
$ vault write sys/policy/dev-team-policy policy=@dev-team-policy.hcl
    
# List the policy 
$ vault list sys/policy
Keys
----
default
dev-team-policy
java-example
jenkins
ops-team-policy
root
```

#### Stage 3 Using the Policy
```bash
# We can test this policy by creating a token and to that token the policy is applied 
    
$ vault token create -policy=dev-team-policy
# outputs a TOKEN-XXXXXXXXXXX
$ vault login TOKEN-XXXXXXXXXXX 
    
# Can perform CRUD Operations
    
$ vault write secret/dev/foo value=bar
$ vault read secret/dev/foo 
$ vault write secret/test/foo value=bar
```