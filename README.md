# 🚀 Kubernetes Monitoring Dashboard

## 📌 Overview

A DevOps project that monitors Kubernetes cluster status using a web dashboard.

## 🛠 Tech Stack

- Flask (Python)
- Docker
- Kubernetes (Minikube)
- Jenkins CI/CD
- GitHub

## 🚀 Features

- CPU & Memory monitoring (mock/demo)
- Pod status display
- Node health monitoring
- CI/CD automation with Jenkins

## ⚙️ CI/CD Pipeline

GitHub → Jenkins → Docker Build → Docker Push → Kubernetes Deploy

## 📦 Run Locally

docker build -t k8s-dashboard .
docker run -p 5000:5000 k8s-dashboard

## ☸ Deploy on Kubernetes

kubectl apply -f k8s/
minikube service dashboard-service
