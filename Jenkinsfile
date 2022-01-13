pipeline {
    agent any
    stages {
        stage("build") {
            when {
                expression {
                    BRANCH_NAME == "master"
                }
            }
            steps {
                echo "building images ..."
                sh 'docker-compose build'
            }
        }
        stage("deploy") {
            steps {
                echo "running containers ..."
                sh 'docker-compose up -d'
            }
        }
    }
}