pipeline {
    agent any

    environment {
        STAGE_URL = 'http://your-staging-app-url.com'  // Change to your staging URL
    }

    stages {
        stage('Build and Deploy') {
            steps {
                // Build WAR file (adjust if using Maven or Gradle)
                sh 'mvn clean package'

                // Deploy WAR (example for Tomcat)
                sh 'cp target/your-app.war /opt/tomcat/webapps/'

                // Restart Tomcat (adjust if needed)
                sh 'sudo systemctl restart tomcat'

                // Wait a few seconds to allow server startup
                sleep 15
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

    post {
        always {
            echo 'Cleaning up virtual environment'
            sh 'rm -rf venv'
        }
    }
}

