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
                    sh '''
                    # Install dependencies globally in the system Python
                    pip install --break-system-packages -r advanced_ai_project/requirements.txt
                    # Optionally, check installed packages for debugging
                    # Check if psycopg2 is installed
                    pip show psycopg2
                    # Optionally, list installed packages for debugging
                    pip list
                    python3 --version
                    '''
                }
            }
        }

        stage('Train Model') {
            steps {
                script {
                    sh '''
                    # Ensure correct Python interpreter is being used
                    python3 --version
                    # Run the training script
                    python3 advanced_ai_project/train_model.py
                    '''
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
