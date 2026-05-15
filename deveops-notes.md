# DevOps Learning Journal

## Initial Understanding

At the beginning of the internship, my understanding of DevOps was mostly limited to the general workflow of building an application, containerizing it, and deploying it to the cloud. Through the internship, I gradually understood how different tools and services connect together to form a real deployment pipeline.

One major realization was that DevOps is not just about deployment, but also about automation, consistency, infrastructure management, debugging, and production reliability.

---

## Linux & AWS EC2 Learnings

I learned how Linux-based cloud servers are managed using AWS EC2 Ubuntu instances. Initially, cloud deployment felt abstract, but working directly with EC2 helped me understand how applications are hosted on remote servers.

Some important concepts learned:

* SSH-based remote server access
* Security groups and port management
* Public IP accessibility
* Difference between local machine and cloud server environments

One interesting learning was understanding why ports like 22, 80, and 5000 are important:

* Port 22 for SSH access
* Port 80 for HTTP traffic
* Port 5000 for the Flask application

I also learned that restarting EC2 instances can change public IP addresses, which later affected the CI/CD deployment pipeline.

---

## Docker & Containerization Learnings

Docker was one of the most important technologies explored during the internship.

Initially, I was confused about the difference between Docker images and containers. Through implementation, I understood:

* Docker image = blueprint/snapshot
* Docker container = running instance of the image

Some key learnings:

* Docker images do not automatically update when source code changes
* Rebuilding is required after application modifications
* Port mapping is necessary to expose applications outside containers
* Containerization helps maintain deployment consistency across environments

One major realization was understanding why Docker is widely used in production systems:
it removes the “works on my machine” problem by packaging applications with their dependencies.

---

## Deployment & Networking Learnings

Deploying applications on AWS EC2 helped me understand several networking concepts that I had previously only heard theoretically.

Important concepts explored:

* Public IP vs localhost
* Port mapping using Docker
* Why applications need to bind to 0.0.0.0
* Security groups and inbound rules
* HTTP traffic routing

One interesting debugging experience involved understanding why the application was inaccessible externally even though the container was running. This helped me understand the role of port exposure and network accessibility.

---

## CI/CD & Automation Learnings

A major part of the internship involved implementing CI/CD pipelines using GitHub Actions.

Initially, I viewed CI/CD as just “automatic deployment,” but later understood the difference between:

* Continuous Integration (CI)
* Continuous Deployment (CD)

The implemented workflow:

1. Push code to GitHub
2. Automatically build Docker image
3. Push image to Docker Hub
4. Connect to EC2 through SSH
5. Pull latest image and restart container

One important realization was how automation reduces repetitive deployment steps and improves consistency.

I also encountered deployment failures during pipeline execution and learned how to debug GitHub Actions logs systematically.

---

## Production Deployment Concepts

Towards the later stages of the internship, I explored production deployment concepts using Gunicorn and Nginx.

Initially, the Flask development server was being used directly. Later, I understood:

* Flask development server is not production-ready
* Gunicorn acts as a production WSGI server
* Nginx works as a reverse proxy in front of the application

The deployment flow evolved into:

Browser → Nginx → Gunicorn → Flask Application

This helped me understand how real-world production deployments are structured.

---

## Debugging & Problem Solving

One of the most valuable parts of the internship was debugging real deployment issues.

Some problems encountered:

* Docker containers exiting unexpectedly
* CI/CD pipeline failures
* Incorrect EC2 public IP stored in GitHub Secrets
* SSH timeout errors during deployment
* Nginx configuration issues
* Application not accessible externally

One major learning was that debugging is a core part of DevOps workflows and that deployment pipelines involve multiple interconnected layers.

---

## Remote Server Management Learnings

I also explored SSH-based remote server management using MobaXterm instead of relying only on browser-based EC2 access.

This helped me understand:

* Persistent SSH workflows
* Remote Linux server management
* Professional deployment workflows used in real environments

---

## Reflections & Key Takeaways

This internship significantly improved my practical understanding of DevOps workflows and cloud deployment practices.

Some major takeaways:

* DevOps involves much more than deployment
* Automation and consistency are critical
* Infrastructure and networking concepts are extremely important
* Debugging and problem-solving are essential skills
* Production deployment architecture differs significantly from local development workflows

The internship also increased my confidence in working with cloud infrastructure, Linux servers, CI/CD pipelines, and containerized deployments.
