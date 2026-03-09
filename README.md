# Agile Lab 1

This repository contains our submission for Agile Lab 1, covering both Task 1 and Task 2.

## Contributors

- Abdallah Mohamed
    
- Ahmed ElSayed
    
- Ahmed Gamal
    
- Muhammed Bassiouni
    
- Omar Gamal
    

---

## Task 1

### Requirements

1. Write a Python function that takes a string and returns the sum of any integers found inside it.
    
2. Develop the code using the Agile Test-Driven Development (TDD) methodology.
    
3. Follow clean code principles.
    

### Our Implementation

The main function logic is located in `sum_digits.py`, and our test cases are in `test_sum_digits.py`. We used the standard `unittest` package for our testing suite.

To ensure our code is clean and maintainable, we applied the following practices:

1. **Code Modularity:** We separated the core logic and testing into distinct modules.
    
2. **Naming:** We used clear, representative names for all variables and functions.
    
3. **Documentation:** We included docstrings for all functions.
    
4. **Comments:** We added inline comments to explain the "why" behind our code.
    

---

## Task 2

### Requirements

Compare Jenkins, AWS CodePipeline, and GitHub Actions based on business use cases, pricing, and deployment settings.

# CI/CD Tools Comparison

## Jenkins

Jenkins is a highly extensible, open-source automation server relying on a massive plugin ecosystem to build, deploy, and automate projects.

- **Business Use Cases:** It is great for custom CI/CD workflows, automating tests on commits, running periodic backups, and integrating with team chat apps like Slack or Teams for build notifications.
    
- **Pricing:** The software itself is 100% free. However, you are responsible for the cost of the server infrastructure hosting it and the engineering time required to maintain it.
    
- **Deployment Settings:** You define stages (usually Build, Test, and Deploy) in a `Jenkinsfile`. It supports manual approvals via an `input` step when pushing to production. Passwords and SSH keys are securely stored in its internal credential manager.
    

## AWS CodePipeline

CodePipeline is a fully managed continuous delivery service built natively into the AWS cloud.

- **Business Use Cases:** It is ideal for enterprise teams already heavily invested in the AWS ecosystem (using EC2, Lambda, Fargate, etc.) who need strict compliance and infrastructure-as-code automation.
    
- **Pricing:** You pay based on active pipelines ($1.00/month for V1) or execution minutes ($0.002/min for V2), with a free tier available. You also pay for the underlying AWS resources (like S3 or CodeBuild) used during runs.
    
- **Deployment Settings:** Pipelines are configured via the AWS Console, CLI, or IaC tools like CloudFormation. Security is handled natively through AWS IAM roles, eliminating the need to manage external API keys. You can easily add manual approval stages via the console or SNS notifications.
    

## GitHub Actions

GitHub Actions is a CI/CD platform that lets you automate workflows directly alongside your code inside your GitHub repository.

- **Business Use Cases:** Perfect for teams wanting a developer-centric, code-first CI/CD setup without a separate dashboard. It relies on community-driven actions to deploy across multi-cloud environments (AWS, Azure, GCP) or publish packages.
    
- **Pricing:** It is completely free and unlimited for public repositories. Private repos get a generous free tier (e.g., 2,000 minutes/month), then switch to a pay-as-you-go model based on the runner's OS.
    
- **Deployment Settings:** Workflows are written entirely in YAML and stored in the `.github/workflows/` directory. You can enforce manual approvals using "Environments" rules. It supports OIDC, allowing secure, keyless authentication to cloud providers.
    

---

## Comparison Table

|**Feature**|**Jenkins**|**AWS CodePipeline**|**GitHub Actions**|
|---|---|---|---|
|**Hosting Model**|Self-hosted (You manage servers)|Fully managed SaaS (AWS)|Fully managed SaaS (GitHub)|
|**Primary Ecosystem**|Open-source plugins|AWS-native services|GitHub repos & multi-cloud|
|**Configuration**|`Jenkinsfile` or Web UI|AWS Console, CLI, or IaC|`.yaml` files in repository|
|**Pricing**|Free (except server infrastructure)|Pay-per-pipeline or per-minute|Free for public repos, generous private tier|
|**Maintenance Burden**|High (Server and plugin updates)|Low (Handled by AWS)|Low (Handled by GitHub)|

## Resources

- [GitHub Actions Website](https://github.com/features/actions)
    
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
    
- [AWS CodePipeline Website](https://aws.amazon.com/codepipeline/)
    
- [AWS CodePipeline Documentation](https://docs.aws.amazon.com/codepipeline/)
    
- [Jenkins Website](https://www.jenkins.io/)
    
- [Jenkins Deployment](https://www.jenkins.io/doc/book/pipeline/)