pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'githubuseraccesstoken', usernameVariable: 'GIT_USER', passwordVariable: 'GIT_PASS')]) {
                    sh 'rm -rf advanced_ai_project'
                    sh 'git clone https://$GIT_USER:$GIT_PASS@github.com/superdoo/advanced_ai_project.git'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Create a virtual environment
                    sh 'python3 -m venv venv'
                    
                    // Activate the virtual environment and install dependencies
                    sh '. venv/bin/activate && pip install -r advanced_ai_project/requirements.txt'
                }
            }
        }

        stage('Check Python Version') {
            steps {
                script {
                    // Check Python version inside virtual environment
                    sh '. venv/bin/activate && python3 --version'
                    sh '. venv/bin/activate && pip show pandas'
                    sh 'pwd'
                }
            }
        }

        stage('Train Model') {
            steps {
                script {
                    // Train the model inside the virtual environment
                    sh '. venv/bin/activate && python3 advanced_ai_project/train_model.py'
                }
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
