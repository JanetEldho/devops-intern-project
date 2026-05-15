# DevOps Cloud Deployment Pipeline using Flask, Docker, AWS EC2 and GitHub Actions

## Overview

This project demonstrates a production-style cloud deployment workflow using Docker, AWS EC2, GitHub Actions CI/CD, Gunicorn, and Nginx reverse proxy integration.

The project was developed as part of a DevOps & Cloud Internship to gain practical exposure to containerization, automated deployment workflows, Linux-based cloud infrastructure, and production deployment concepts.

---

## Features

- Flask-based backend application
- Docker containerization
- AWS EC2 cloud deployment
- GitHub Actions CI/CD pipeline
- Docker Hub image integration
- Automated deployment using shell scripts
- Gunicorn production server setup
- Nginx reverse proxy integration
- SSH-based remote server management

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python & Flask | Backend application |
| Docker | Containerization |
| AWS EC2 | Cloud hosting |
| GitHub Actions | CI/CD automation |
| Docker Hub | Container registry |
| Linux (Ubuntu) | Server management |
| Gunicorn | Production WSGI server |
| Nginx | Reverse proxy |
| MobaXterm | SSH-based remote access |

---

## Project Architecture

```text
Developer
↓
GitHub Repository
↓
GitHub Actions CI/CD Pipeline
↓
Docker Image Build
↓
Docker Hub
↓
AWS EC2 Instance
↓
Nginx Reverse Proxy
↓
Gunicorn Server
↓
Flask Application
```

---

## CI/CD Workflow

1. Code changes are pushed to GitHub.
2. GitHub Actions automatically triggers the workflow.
3. Docker image is built from the application source code.
4. The image is pushed to Docker Hub.
5. GitHub Actions connects to the EC2 instance using SSH.
6. The deployment script pulls the latest image and restarts the container.
7. Nginx forwards incoming traffic to the Gunicorn server running the Flask application.

---

## Implementation Highlights

- Configured AWS EC2 instances and security groups for cloud deployment.
- Built Docker images and managed containers for application deployment.
- Automated deployment workflows using GitHub Actions.
- Implemented deployment automation using shell scripting.
- Explored production deployment concepts using Gunicorn and Nginx.
- Used SSH-based remote server management workflows through MobaXterm.

---

## Challenges Faced

- Debugging Docker container startup failures.
- Managing EC2 networking and port configurations.
- Handling changing EC2 public IP addresses affecting deployment workflows.
- Understanding reverse proxy configuration using Nginx.
- Debugging CI/CD pipeline failures and deployment issues.

---

## Future Improvements

- Explore Amazon ECS and Kubernetes orchestration.
- Add HTTPS and domain-based deployment.
- Implement monitoring and logging solutions.
- Extend CI/CD pipeline with automated testing.

---

## Screenshots

### Application UI
(Add screenshot here)

### GitHub Actions CI/CD Pipeline
(Add screenshot here)

### AWS EC2 Deployment
(Add screenshot here)

### Nginx Reverse Proxy Setup
(Add screenshot here)

---

## Repository Structure

```text
.
├── .github/workflows/
├── screenshots/
├── app.py
├── Dockerfile
├── deploy.sh
├── README.md
└── WORK_LOG.md
```

---

## Learning Outcomes

This project provided practical exposure to:
- DevOps workflows
- Containerization
- Cloud deployment
- Linux server management
- CI/CD automation
- Production deployment architecture

---

## Author

Janet Eldho