pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                sh 'echo "Checkout Success!"'
            }
        }
        stage('Lint Python') {
            steps {
                sh 'pylint --disable=R,C *.py application/*.py'
            }
        }
    }
}