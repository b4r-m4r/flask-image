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
                    powershell 'echo $DOCKER_PASSWORD test?> c:\\temp\\test.txt'
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
