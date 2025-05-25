pipeline {
    agent {
        docker {
            image 'python:3.10'
            args '-u root' // se precisar instalar libs do sistema
        }
    }

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Instalar Dependências') {
            steps {
                sh 'python -m venv $VENV_DIR'
                sh './$VENV_DIR/bin/pip install --upgrade pip'
                sh './$VENV_DIR/bin/pip install -r requirements.txt'
            }
        }

        stage('Rodar Testes') {
            steps {
                sh './$VENV_DIR/bin/pytest tests/'
            }
        }
    }

    post {
        success {
            echo '✅ Testes passaram com sucesso.'
        }
        failure {
            echo '❌ Testes falharam!'
        }
    }
}