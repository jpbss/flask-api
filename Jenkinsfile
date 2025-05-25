pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }

        stage('Install dependencies'){
            agent{
                docker {
                    image 'node:18-alpine'
                }
            }
            steps{
                sh 'node --version'
            }
        }
    }
}
