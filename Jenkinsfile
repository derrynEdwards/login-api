pipeline {
    environment {
        image_repo = "xwindwolfx/login-api"
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
        stage('Copy Config Files to S3 Bucket') {
            steps {
                withAWS(region:'us-west-2',credentials:'AWS Jenkins') {
                    sh 'echo "Uploading content with AWS creds"'
                    s3Upload(pathStyleAccessEnabled: true, payloadSigningEnabled: true, file:'aws/config/', bucket:'login-api')
                }
            }
        }
        stage('Build and Push Docker Image') {
            steps {
                echo 'Starting to build docker image'
                sh 'cp .env-sample .env'
                script {
                    def dockerImage = docker.build(image_repo)
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                        dockerImage.push("1.0.$BUILD_NUMBER")
                        dockerImage.push("latest")
                    }
                }
            }
        }
        stage('Deploy API on AWS') {
            steps {
                sh 'chmod +x ./aws/create.sh'
                script {
                    try {
                        sh './aws/create.sh loginapi-net loginapi-network.yml loginapi-network-params.json'
                        sh './aws/create.sh loginapi-web loginapi-server.yml loginapi-servers-params.json'
                    }
                    catch(err) {
                        echo 'CF Stack already deployed, now updating cluster.'
                    }
                }
            }
        }
    }
}