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
                usernameVariable: 'dockerUser', passwordVariable: 'dockerPass')]) 
                {
                    powershell 'echo $dockerPass | docker login -u $dockerUser --password-stdin'
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
