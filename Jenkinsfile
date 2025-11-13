pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install --break-system-packages -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                    export PATH=$PATH:/var/jenkins_home/.local/bin
                    export PYTHONPATH=$PYTHONPATH:$(pwd)
                    pytest tests/
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t python-jenkins-demo .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker stop python-demo || true'
                sh 'docker rm python-demo || true'
                sh 'docker run -d --name python-demo -p 5001:5001 python-jenkins-demo'
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: '**/*.py', fingerprint: true
            }
        }
    }
}
