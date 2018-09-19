# The complexity of managing secrets
For building any cloud infrastructure application or deployment where everything is self-serviced or fully automated, 
the below questions are always the pain point for an infra engineer.  
1. How to securely share secret management responsibility among a set of stakeholders across the organization ?
2. How to allow seamless access to both humans and services ?
3. How to audit who accessed a secret at a certain date and time ?
4. How to handle external and internal threats (like hackers) ?

When we have Infrastructure as a Code why should't we have Authorization as a Code :)


## Hashicorp Vault
Hashicorp Vault is an open source secret management and distribution tool that proposes answer to the above questions.
Its a Cloud friendly application build to manage all types of secret.
The main features of the Hashicorp Vault’s are.

1. Dynamic secrets: 
    * Vault is able to generate credentials automatically for different backends.
2. Mitigation of internal and external threats: 
    * Allowing Vault to be sealed/unsealed in response to crises, and supporting a variety of security backends.
3. Lease renewal/revoke access to secrets: 
    * Vault allows you to specify TTL rules for a secret, enabling fine control over permissions.
4. Auditing: 
    * Once enabled, every secret request will be logged, with the output directed to a file or to syslog.

## Backends
Vault offers modular plug-in for three main areas: 
   * Encrypted secret storage
   
        This is the solution that will “host” the secrets. Available backends include AWS S3, Consul, Generic (file storage), among others.
   * Authentication controls
   
        The authentication mechanism used. Available backends are AWS EC2, LDAP, Github, Tokens, Username/password, and others.
   * Audit logs.
   
        Where logs are sent. Available File or syslog. The specific mix of backends will depend on your project’s requirements and constraints, and more than one backend can be enabled.
 
 
 
 
 
 