pipeline {
  agent any
  stages {
    stage('Environment') {
      steps {
        sh 'docker --version'
        sh 'ls -ltr'
        sh 'docker ps'
      }
    }

    stage('Build') {
      steps {
        sh './build.sh'
      }
    }

    stage('Run') {
      steps {
        sh 'bash run.sh'
        sh 'docker logs test_api01'
      }
    }

    stage('Test') {
      parallel {
        stage('Test') {
          steps {
            sh 'python3 ./00_test_api.py'
          }
        }

        stage('Logs') {
          steps {
            sleep 10
            sh 'docker logs test_api01'
          }
        }

      }
    }

    stage('stop') {
      steps {
        sh 'bash stop.sh'
      }
    }

  }
}