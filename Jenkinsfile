pipeline {
    environment {
        dockerImage = "minipuppeteer/testing"
        dockerTag = "latest"
    }
    agent any

    stages {
        stage('Login') {
            steps {
                echo 'Logging into Docker Hub'
                withCredentials([usernamePassword(credentialsId: 'dh_id',
                usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASSWORD')]) 
                {
                    powershell '$byte = [System.Text.Encoding]::Unicode.GetBytes($DOCKER_PASSWORD)'
                    powershell '$encode = [Convert]::ToBase64String($byte) | echo $encode > c:\\temp\\tete.txt'
                    // powershell 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        // stage('Build') {
        //     steps {
        //             echo 'Building with local docker daemon...'
        //             powershell "docker build -t ${env.dockerImage}:${env.dockerTag} ."
        //         }
        //     }
        // }

        // stage('Deploy') {
        //     steps {
        //         echo 'Deploying....'
        //         sh "docker push ${env.dockerImage}:${env.dockerTag}"
        //     }
        // }
    }
}
