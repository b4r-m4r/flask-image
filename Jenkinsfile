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
                    echo 'Building with local docker daemon...'
                    powershell "docker build -t ${env.dockerImage}:${env.dockerTag} ."
                }
            }
        }

        // stage('Deploy') {
        //     steps {
        //         echo 'Deploying....'
        //         sh "docker push ${env.dockerImage}:${env.dockerTag}"
        //     }
        // }
    }
