pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Checkout code from Github repository
                git branch: 'main', url: 'https://github.com/Alixab98/Restful_app'

                // Build Docker image
                script {
                    sh 'docker build -t rest_app .'
                    
                }
            }
        }

        stage('Test') {
            steps {
                // Run unit tests
                sh 'pytest app/flaskapp/test.py'
            }
        }

    post {
    always {
      sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
      sh 'docker push my-rest_app'
                }
            }
        }
    }

    
}
