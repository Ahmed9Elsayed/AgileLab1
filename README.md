# Agile Lab 1

This is the submission for Agile Lab 1

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

### Our Research
#### Jenkins

##### Definition
Jenkins is an automation server that provides hundreds of plugins to support building, deploying, and automating any project

Some of the features that are included in Jenkins are:
 1. Easy Installation and Configuration
 2. Plugins
 3. Extensible
 4. Distributed

#### Business Use Cases
CI: Jenkins can automate the process of building and testing code every time a developer commits a change

CD: Jenkins can orchestrate the deployment of the applications to various environments (eg. staging, testing, production)

Jenkins can also run periodic data backups, collect statistics about service, and run security scans

Jenkins can be integerated with communication platforms like Slack or Microsoft Teams to notify team members about build and test results

#### Pricing
Jenkins is free open-source platform that requires no fees to deal with

The only payment may occur in the infrastructure that will host it and the maintenance of it

#### Deployment Settings
The most basic continuous delivery pipeline will have, at minimum, three stages which should be defined in a Jenkinsfile: Build, Test, and Deploy.

Often when passing between stages, especially environment stages, you may want human input before continuing. For example, to judge if the application is in a good enough state to "promote" to the production environment. This can be accomplished with the input step in Jenkinsfile.

Jenkins must have credentials (SSH, user/password, tokens) saved in its credential manager to securely log into servers or cloud platforms.

## Resources
1. [Jenkins Website](https://www.jenkins.io/)

2. [Jenkins Deployment](https://www.jenkins.io/doc/pipeline/tour/deployment/)
