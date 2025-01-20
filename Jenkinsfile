pipeline {
    environment {
        dockerImage = "minipuppeteer/testing"
        dockerTag = "latest"
        DOCKER_CRDS = credentials('dh_id')
    }
    agent any

    stages {
        stage('Login') {
            steps {
                echo 'Logging into Docker Hub'
                powershell('echo $DOCKER_CRDS_PSW | docker login -u $DOCKER_CRDS_USR --password-stdin')
                
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