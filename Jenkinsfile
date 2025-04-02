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

    stage('Install Dependencies and Train Model') {
    steps {
        script {
            sh '''
            # Create and activate the virtual environment
            python3 -m venv venv
            . venv/bin/activate

            # Install dependencies
            pip install --break-system-packages -r advanced_ai_project/requirements.txt
            
            # Debug the Python environment
            which python
            which pip
            pip list
            
            # Train the model using the virtual environment's Python interpreter
            venv/bin/python3 advanced_ai_project/train_model.py
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
