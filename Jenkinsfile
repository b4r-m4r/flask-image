pipeline {
    environment {
        dockerImage = "minipuppeteer/testing"
        dockerTag = "latest"
    }
    agent any

    stages {
        stage('Login') {
            environment {
                DOCKER_CRDS = credentials('dh_id')
            }
            steps {
                sh('echo $DOCKER_CRDS_PSW | docker login -u $DOCKER_CRDS_USR --password-stdin')
            }

        stage('Build') {
            steps {
                    echo 'Building with local docker daemon...'
                    sh "docker build -t ${env.dockerImage}:${env.dockerTag} ."
                }
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh "docker push ${env.dockerImage}:${env.dockerTag}"
            }
        }
    }
}