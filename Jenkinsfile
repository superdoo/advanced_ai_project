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
                stage('Remove Non-Python 3 Versions') {
            steps {
                script {
                    // List all Python versions installed and remove non-Python 3 versions
                    sh '''
                    # List all Python binaries installed
                    python_versions=$(ls /usr/bin/python* | grep -v "python3")

                    # Remove all non-Python 3 versions
                    for version in $python_versions; do
                        echo "Removing $version..."
                        sudo apt-get remove --purge -y $version
                    done

                    # Confirm remaining Python versions
                    echo "Remaining Python versions:"
                    python3 --version
                    '''
                }
            }
        }



        stage('Install Dependencies') {
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
            '''
        }
    }
}

        stage('Train Model') {
    steps {
        script {
            sh '''
            # Make sure to use the virtual environment's Python interpreter
            . venv/bin/activate
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
