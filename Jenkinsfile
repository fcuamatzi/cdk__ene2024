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

  }
}