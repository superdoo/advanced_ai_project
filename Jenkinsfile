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
            python3 -m venv venv
            . venv/bin/activate
            pip install --break-system-packages -r advanced_ai_project/requirements.txt
            python3 -m site  # Show the Python site packages being used
            '''
        }
    }
}

stage('Train Model') {
    steps {
        script {
            sh '''
            # Activate the virtual environment
            . venv/bin/activate
            # Print Python version and paths for debugging
            python3 --version
            which python3
            python3 train_model.py
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
