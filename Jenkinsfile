pipeline {
    environment {
        dockerImage = "minipuppeteer/testing"
        dockerTag = "latest"
        registryCredential = 'dh_id'
    }
    agent any

    stages {
        stage('Login') {
            steps {
                echo 'Logging into Docker Hub'
                withCredentials([usernamePassword(credentialsId: $registryCredential,
                usernameVariable: 'dockerUser', passwordVariable: 'dockerPass')]) 
                {
                    powershell "echo $dockerPass | docker login -u $dockerUser --password-stdin"
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
