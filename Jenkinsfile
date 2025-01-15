pipeline {
    environment {
        dockerImage = "minipuppeteer/testing"
        dockerTag = "latest"
        registryCredential = 'dh_id'
    }
    agent {
        kubernetes {
            podTemplate(
                agentContainer: 'docker',
                agentInjection: true,
                yaml: '''
                    apiVersion: v1
                    kind: Pod
                    spec:
                    containers:
                    - name: docker
                        image: docker:dind
                ''')
        }
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh docker.build("${dockerImage}:${dockerTag}")
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
