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
                - "--destination=${dockerImage}:${dockerTag}"
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
                container('kaniko') {
                    echo 'Building with Kaniko...'
                    sh "/kaniko/executor --context=/workspace --dockerfile=/workspace/Dockerfile --destination=${dockerImage}:${dockerTag}"
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
