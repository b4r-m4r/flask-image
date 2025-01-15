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
                batchFile "docker build -t ${dockerImage}:${dockerTag} ."
            }
        }

        stage('Login') {
            steps {
                echo 'Logging in..'
                withCredentials([usernamePassword(credentialsId: registryCredential, usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    batchFile """
                        echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                    """
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying....'
                batchFile "docker push ${dockerImage}:${dockerTag}"

            }
        }
    }
}
