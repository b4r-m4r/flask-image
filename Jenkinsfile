pipeline {
    environment {
        dockerImage = "minipuppeteer/testing"
        dockerTag = "latest"
        registryCredential = 'dh_id'
    }
    agent {
        kubernetes {
            yaml """
            apiVersion: v1
            kind: Pod
            spec:
              containers:
              - name: docker
                image: docker:20.10.24
            """
        }
    }
    }

    stages {
        stage('Build') {
            steps {
                container('docker') {
                    echo 'Building..'
                    sh docker.build("${dockerImage}:${dockerTag}")
                }
            }
        }

        // stage('Deploy') {
        //     steps {
        //         echo 'Deploying....'
        //         sh "docker.Image.push(${dockerTag})"

        //     }
        // }
    }
}
