/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'python:3.6.8' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'pip install -r requirements.txt'
                sh 'python manage.py test accounts lists'
                sh 'pip install selenium fabric3'
                sh 'python  manage.py test functional_tests'
            }
        }
    }
}
