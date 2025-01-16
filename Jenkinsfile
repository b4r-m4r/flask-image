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
              - name: kaniko
                image: gcr.io/kaniko-project/executor:latest
                args:
                - "--dockerfile=/workspace/Dockerfile"
                - "--context=/workspace"
                - "--destination=${env.dockerImage}:${env.dockerTag}"
                volumeMounts:
                - name: docker-config
                  mountPath: /kaniko/.docker
              volumes:
              - name: docker-config
                secret:
                  secretName: docker-registry-secret
            """
        }
    }

    stages {
        stage('Build') {
            steps {
                checkout scm
                container('kaniko') {
                    echo 'Building with Kaniko...'
                    sh "/kaniko/executor --context=/workspace --dockerfile=/workspace/Dockerfile --destination=${env.dockerImage}:${env.dockerTag}"
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
}
