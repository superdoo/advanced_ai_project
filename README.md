# AI-Powered Data Pipeline with Full CI/CD (No AWS Required)

This advanced project builds a local, production-grade, AI-powered data pipeline with a complete CI/CD lifecycle—no cloud services required.

---

## Overview

This project showcases a fully automated system that:

- Trains a machine learning model using customer data from PostgreSQL
- Automates the pipeline via GitHub → Jenkins → Docker
- Serves real-time predictions using FastAPI, secured and load-balanced behind Nginx
- Uses Terraform for local infrastructure-as-code deployment

---

## Tech Stack

- VS Code – Development Environment  
- Python – Data Processing & ML Model  
- GitHub – Version Control  
- Jenkins – CI/CD Automation  
- Docker & Docker Compose – Containerization  
- PostgreSQL – Database  
- FastAPI + Nginx – Real-Time Inference & Reverse Proxy  
- Terraform – Local Infrastructure Automation  

---

## CI/CD Workflow

1. Code is developed and pushed to GitHub.
2. Jenkins pulls the latest code, trains the model, builds a Docker image, and spins up services.
3. FastAPI serves a `/predict` API endpoint.
4. Nginx handles reverse proxying and load balancing.
5. Terraform provisions the local environment.

---

## Highlights

- End-to-End CI/CD on Local Infrastructure  
- Real-Time AI Model Deployment  
- Infrastructure-as-Code with Terraform  
- Lightweight, Scalable, and Cloud-Free  
- Modular, Maintainable Design  

---

## Ideal For

- DevOps and ML Engineers seeking local CI/CD pipeline practice  
- AI projects requiring real-time serving without cloud lock-in  
- Learning advanced automation and infrastructure tools

---

## Customization

This project can be extended with features like user authentication, GPU acceleration, monitoring tools, or integration with other data sources.

---

**License**:  
**completed by**: Michael Barreras
