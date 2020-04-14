pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                sh 'echo "Checkout Success!"'
            }
        }
        stage('Setup') {
            steps {
                sh '''
                    python3 -m venv ~/.login-api
                    . ~/.login-api/bin/activate
                    pip install --upgrade pip
                    pip install --trusted-host pypi.python.org -r requirements.txt
                   '''
            }
        }
        stage('Lint Python') {
            steps {
                sh '''
                    . ~/.login-api/bin/activate
                    pylint --disable=R,C *.py application/*.py
                   '''
            }
        }
    }
}