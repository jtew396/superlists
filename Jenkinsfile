/* Requires the Docker Pipeline plugin */
pipeline {
    agent none

    stages {
        stage('build') {
            agent {
                docker {
                    image 'python:3.6.8-alpine'
                }
            }
            steps {
                sh 'python3 --version'
                sh 'pip install -r requirements.txt'
                sh 'python3 manage.py test accounts lists'
                sh 'pip install selenium fabric3'
                sh 'python3  manage.py test functional_tests'
            }
        }
    }
}
