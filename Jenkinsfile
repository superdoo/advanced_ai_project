
pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/yourusername/ai_data_pipeline.git'
            }
        }
        stage('Train Model') {
            steps {
                sh 'python train_model.py'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ai-pipeline .'
            }
        }
        stage('Run Docker Compose') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}