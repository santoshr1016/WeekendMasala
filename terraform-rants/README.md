 **What is** `Terraform`
 
 Terraform lets you define your own Infra as Code.
 You can build, change and version it safely and efficiently.
 
 General Problems in Manual configurations.
 1. Error prone.
 2. Time consuming. You just cannot sit clicking the console UI for a complex infra.
 3. Very difficult to create identical multiple infra env(Dev, Stage, Prod)
 4. Keeping the env upto-date
 
 Advantages of Terraform
 1. Very Fast, You just define your infra and boom its real.
 2. As infra is defined as Code, You can use version control. _Check my PR for load balancers plz_
 3. Reproducible everytime you create an env, it will be exactly the same.
 4. Terraform allows you to plan before applying changes
 5. Uses the provider model - AWS
                            - Azure
                            - Google Cloud
    What it means, I can mix up. _Can I have EC2 in AWS, ELB in Azure and DB in GC_
 6. Destroy infra quickly.
 7. Import the existing infra.
 8. Big open source vibrant community
 
 With this start you can find the sample snippets to help understand better TF.