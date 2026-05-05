pipeline {
    agent any

    environment {
        IMAGE = "tominsahu/k8s-dashboard"
        TAG = "latest"
        KUBECONFIG = "C:\\Users\\Dell\\.kube\\config"
    }

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Tomin-sahu/k8s-monitoring-dashboard.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE%:%TAG% ."
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'sahutomin94@gmail.com',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {
                    bat "echo %PASS% | docker login -u %USER% --password-stdin"
                }
            }
        }

        stage('Push Image') {
            steps {
                bat "docker push %IMAGE%:%TAG%"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat "kubectl apply -f k8s/deployment.yaml"
                bat "kubectl apply -f k8s/service.yaml"
            }
        }

        stage('Verify Deployment') {
            steps {
                bat "kubectl get pods"
                bat "kubectl get svc"
            }
        }
    }

    post {
        success {
            echo "🚀 Deployment Successful"
        }
        failure {
            echo "❌ Deployment Failed"
        }
    }
}
