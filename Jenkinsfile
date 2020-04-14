pipeline {
    environment {
        image_repo = "xwindwolfx/login-api"
        image_cred = "dockerhub"
    }
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
                    pylint --load-plugins pylint_flask,pylint_flask_sqlalchemy --disable=R,C *.py application/*.py
                   '''
            }
        }
        stage('Lint Dockerfile') {
            steps {
                sh 'hadolint Dockerfile'
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Starting to build docker image'
                script {
                    def dockerImage = docker.build(image_repo)
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                withDockerRegistry([ credentialsId: "dockerhub" ]) {
                    dockerImage.push("$BUILD_NUMBER")
                    dockerImage.push("lastest")
                }
            }
        }
    }
}