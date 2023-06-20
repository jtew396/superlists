/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'python:3.6.8' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                pip install -r requirements.txt
                python manage.py test accounts lists
                pip install selenium fabric3
                python  manage.py test functional_tests
            }
        }
    }
}
