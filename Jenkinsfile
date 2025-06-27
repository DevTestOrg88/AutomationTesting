
pipeline {
    agent any
    tools {
  maven 'mavenversion3.9.10'
}
stages {
  stage('CheckoutCode') {
    steps {
      // One or more steps need to be included within the steps block.
      git branch: "master", url: 'https://github.com/DevTestOrg88/maven-web-application.git'
    }
  }
  stage('Build') {
    steps {
      // One or more steps need to be included within the steps block.
      sh 'mvn clean install'
    }
  }
//Used Snippet Generator with 'Deploy comtainer plugin ' under sample steps and converted to Declarative way scipt using chartGpt
  stage('Deploy to Tomcat') {
            steps {
                step([$class: 'DeployPublisher',
                    adapters: [
                        [$class: 'Tomcat9xAdapter',
                         credentialsId: '4aff5716-dda4-4c4f-8dff-d14020358397',
                         url: 'http://13.203.79.48:9090/manager/text',
                         path: '',
                         alternativeDeploymentContext: ''
                        ]
                    ],
                    contextPath: '/maven-web-application',
                    war: '**/maven-web-application.war'
                ])
            }
        }
    sleep 10
    stage('CheckoutCodeAutomationCode') {
    steps {
      git branch: "master", url: 'https://github.com/DevTestOrg88/TestProject.git'
    }
  }
    stage('Run Selenium Tests') {
            steps {
                // Setup python environment, install dependencies and run test
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    python test_login.py ${STAGE_URL}
                '''
            }
        }
}
// To ensure notifications (like email) run regardless of earlier failures
    post {
            always {
                emailext (
                    attachLog: true,
                    body: 'Check console output at $BUILD_URL to view the results.',
                    subject: '$PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS!',
                    to: 'rajdeeprm88@gmail.com'
                )
            }
        }
}
