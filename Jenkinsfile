pipeline {
    environment {
        dockerImage = "minipuppeteer/testing"
        dockerTag = "latest"
        registryCredential = 'dh_id'
    }
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh "docker build -t ${dockerImage}:${dockerTag} ."
            }
        }

        stage('Login') {
            steps {
                echo 'Logging in..'
                withCredentials([usernamePassword(credentialsId: registryCredential, usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh """
                        echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                    """
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh "docker push ${dockerImage}:${dockerTag}"

            }
        }
    }
}
