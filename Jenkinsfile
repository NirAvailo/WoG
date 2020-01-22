pipeline {
  agent {
    node {
      label 'any'
      customWorkspace 'C:\\Users\\Nir\\PycharmProjects\\WoG'
    }
  }
  stages {
    stage('checkout') {
        steps {
            echo 'https://github.com/NirAvailo/WoG.git'
        }
    }
    stage('build') {
        steps {
            bat 'docker build --compress --no-cache -t wog_app .'
        }
    }
    stage('run') {
        steps {
            bat 'docker container stop wog_app | exit 0'
            bat 'docker container rm -f wog_app | exit 0'
            bat 'docker run --rm -d -p 8777:5000 --name wog_app wog_app'
            sleep 3 // seconds
        }
    }
    stage('test') {
        steps {
            bat 'pip install flask'
            bat 'python e2e.py'
        }
    }
    stage('terminate') {
        steps {
            bat 'docker container stop wog_app'
            bat 'docker container rm -f wog_app'
        }
    }
  }
}