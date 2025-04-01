
pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'githubuseraccesstoken', usernameVariable: 'GIT_USER', passwordVariable: 'GIT_PASS')]) {
                sh 'git clone https://$GIT_USER:$GIT_PASS@github.com/superdoo/ai_data_pipeline.git'
        }
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