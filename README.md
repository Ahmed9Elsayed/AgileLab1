# Agile Lab 1

This is the submission for Agile Lab 1.

You will find Task 1 and Task 2 details in this repository.

## Contributors:
 - Abdallah Mohamed
 - Ahmed ElSayed
 - Ahmed Gamal
 - Muhammed Bassiouni
 - Omar Gamal

## Task 1

### Task 1 Requirements
 1. Create a simple python function that takes a string and returns sum of integers inside this string
 2. Apply Agile Test-Driven Development Methodolgy on your code
 3. Ensure using clean code in your project

### Our Implementation

We implement the code of the function in `sum_digits.py` file and the test code inside `test_sum_digits.py` file

We use `unittest` package for our testing code

We apply different clean code principles in our code:
 1. Code Modularity (Module for testing, and a Module for the function)
 2. Representative variables and function naming
 3. Docstrings for all functions
 4. Comments for in-code explaination

## Task 2

### Task 2 Requirements
Compare between the following CI/CD tools: `Jenkins`, `AWS Code Pipeline`, and `Github` in terms of:
 1. Business Use Cases
 2. Pricing
 3. Deployment Settings


# CI-CD Tools Comparison 

## Jenkins

### Definition

Jenkins is an automation server that provides hundreds of plugins to support building, deploying, and automating any project.

Some of the features that are included in Jenkins are:

- Easy Installation and Configuration
    
- Plugins
    
- Extensible
    
- Distributed

### Business Use Cases

- **CI:** Jenkins can automate the process of building and testing code every time a developer commits a change.
    
- **CD:** Jenkins can orchestrate the deployment of the applications to various environments (eg. staging, testing, production).
    
- Jenkins can also run periodic data backups, collect statistics about service, and run security scans.
    
- Jenkins can be integrated with communication platforms like Slack or Microsoft Teams to notify team members about build and test results.
### Pricing

- Jenkins is a free open-source platform that requires no fees to deal with.
    
- The only payment may occur in the infrastructure that will host it and the maintenance of it.
### Deployment Settings

- The most basic continuous delivery pipeline will have, at minimum, three stages which should be defined in a `Jenkinsfile`: Build, Test, and Deploy.
    
- Often when passing between stages, especially environment stages, you may want human input before continuing. For example, to judge if the application is in a good enough state to "promote" to the production environment. This can be accomplished with the `input` step in Jenkinsfile.
    
- Jenkins must have credentials (SSH, user/password, tokens) saved in its credential manager to securely log into servers or cloud platforms.

---

## AWS CodePipeline

### Definition

AWS CodePipeline is a fully managed continuous delivery service that helps you automate your release pipelines for fast and reliable application and infrastructure updates natively within the Amazon Web Services cloud.

### Business Use Cases

- **CI:** Automates the build and test phases (usually pairing with AWS CodeBuild) whenever code changes are pushed to AWS CodeCommit, GitHub, or Bitbucket.
    
- **CD:** Orchestrates complex deployments to AWS compute services like Amazon EC2, AWS Fargate, AWS Lambda, or on-premises servers (pairing with AWS CodeDeploy).
    
- Ideal for enterprise organizations already heavily invested in the AWS ecosystem that require strict compliance, infrastructure-as-code automation, and deep integration with AWS tools.
### Pricing

- AWS CodePipeline charges based on active pipelines ($1.00 per active V1 pipeline/month) or execution minutes ($0.002 per action execution minute for V2).
    
- The AWS Free Tier includes one free active V1 pipeline per month or 100 free V2 action execution minutes per month.
    
- Additional costs are incurred for the underlying AWS resources used during the pipeline's execution, such as storage (Amazon S3) and compute time (AWS CodeBuild).
### Deployment Settings

- Pipelines are constructed using sequential or parallel stages configured via the AWS Management Console, AWS CLI, or defined as code using AWS CloudFormation or the AWS CDK.
    
- Manual approval actions can be added to any stage to pause the execution until an authorized user approves or rejects the deployment via the console or an SNS notification.
    
- Security is handled natively through AWS Identity and Access Management (IAM) roles, granting the pipeline specific, granular permissions to interact with other AWS services without managing external API keys.

---

## GitHub Actions

### Definition

GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipelines directly alongside your code within your GitHub repository.

### Business Use Cases

- **CI:** Automatically triggers virtual machines to build and test code on almost any GitHub event, such as creating a pull request, pushing a commit, or opening an issue.
    
- **CD:** Deploys applications across multiple cloud providers (AWS, Azure, GCP) or publishes packages (npm, Docker Hub) using thousands of pre-built, community-driven actions.
    
- Ideal for modern development teams ranging from startups to enterprises looking for a developer-centric, code-first CI/CD platform that eliminates the need for a separate CI/CD dashboard.
### Pricing

- GitHub Actions is 100% free and unlimited for public repositories.
    
- Private repositories receive a generous free tier (e.g., 2,000 free minutes and 500 MB of storage per month for standard GitHub Free accounts).
    
- Beyond the free limits, pricing is pay-as-you-go based on the operating system of the runner (Linux is cheapest, followed by Windows, then macOS).
### Deployment Settings

- Workflows are defined entirely via YAML files stored directly in your repository under the `.github/workflows/` directory.
    
- GitHub Actions uses "Environments" to manage deployments. You can set environment protection rules, which require manual approval from designated teams or users before a deployment job can proceed.
    
- It supports OpenID Connect (OIDC), allowing you to securely authenticate with cloud providers to request short-lived access tokens, completely removing the need to store long-lived secret keys in GitHub.

---

## Comparison Table

|**Feature**|**Jenkins**|**AWS CodePipeline**|**GitHub Actions**|
|---|---|---|---|
|**Hosting Model**|Self-hosted (You manage servers)|Fully managed SaaS (AWS)|Fully managed SaaS (GitHub)|
|**Primary Ecosystem**|Open-source plugins for any tool|AWS-native services|GitHub repositories & multi-cloud|
|**Configuration**|`Jenkinsfile` (Groovy) or Web UI|AWS Console, CLI, or CloudFormation|`.yaml` files in repository|
|**Base Pricing**|100% Free (You pay for server infrastructure)|Pay-per-pipeline or per-minute|Free for public repos, generous free tier for private|
|**Maintenance Burden**|High (Server patching, plugin updates)|Low (Handled by AWS)|Low (Handled by GitHub)|

## Resources

- [GitHub Actions Website](https://github.com/features/actions)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [AWS CodePipeline Website](https://aws.amazon.com/codepipeline/)
- [AWS CodePipeline Documentation](https://docs.aws.amazon.com/codepipeline/)
- [Jenkins Website](https://www.jenkins.io/)
- [Jenkins Deployment](https://www.jenkins.io/doc/book/pipeline/)