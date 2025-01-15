pipeline {
    environment {
        registry = "minipuppeteer/testing"
        registryCredential = 'dh_id'
        dockerImage = ''
    }
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                script {
                dockerImage = docker.build registry + ':latest'
                }
                // sh 'docker build -t docker-flask .'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                script {
                docker.WithReigstry('', registryCredential) {
                    dockerImage.push()
                }
                }
                // sh 'docker push '

            }
        }
    }
}
