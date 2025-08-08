pipeline {
    agent any

    environment {
        JAVA_HOME = "C:\\Program Files\\Java\\jdk-17"
        SONAR_TOKEN = credentials('jenkins-token') // Jenkins stored Sonar token
        DOCKER_IMAGE = "myapp:latest" // Change this to your desired image name and tag
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    extensions: [],
                    userRemoteConfigs: [[
                        url: 'https://github.com/Kezara666/jenkins-test-trigger-github-test-soracube-run-docker'
                    ]]
                ])
            }
        }

        stage('Run SonarQube Analysis') {
            steps {
                script {
                    // Run sonar-scanner bat, mark status
                    try {
                        bat """
                        set PATH=%JAVA_HOME%\\bin;%PATH%
                        sonar-scanner.bat ^
                          -Dsonar.projectKey=jenkins-test-trigger ^
                          -Dsonar.projectName=jenkins-test-trigger ^
                          -Dsonar.sources=. ^
                          -Dsonar.python.version=3 ^
                          -Dsonar.host.url=http://localhost:9000 ^
                          -Dsonar.login=%SONAR_TOKEN%
                        """
                        env.SONAR_SUCCESS = "true"
                    } catch (err) {
                        env.SONAR_SUCCESS = "false"
                        error("SonarQube analysis failed.")
                    }
                }
            }
        }

        stage('Build Docker Image') {
            when {
                expression { env.SONAR_SUCCESS == "true" }
            }
            steps {
                bat "docker build -t %DOCKER_IMAGE% ."
            }
        }

        stage('Run Docker Container') {
            when {
                expression { env.SONAR_SUCCESS == "true" }
            }
            steps {
                bat "docker run --rm %DOCKER_IMAGE%"
            }
        }
    }

    post {
        always {
            script {
                if (env.WORKSPACE) {
                    node {
                        cleanWs()
                    }
                } else {
                    echo "No workspace to clean."
                }
            }
        }
        failure {
            echo 'Build failed, skipping Docker build and run steps.'
        }
    }
}
