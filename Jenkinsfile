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
                docker{
                    image 'python:3'
                }
            }
            steps{
                sh 'python3 --version'
            }
        }
    }
}
