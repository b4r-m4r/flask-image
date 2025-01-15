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
                sh "docker.build(${dockerImage}:${dockerTag})"
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh "docker.Image.push(${dockerTag})"

            }
        }
    }
}
