pipeline{  
    agent any
    stages{
      stage('version'){
            steps{
              sh 'python3 --version'
            }
        }
      stage('run python script'){
            steps{
              sh 'python3 simple_common_decorator.py'
            }
        }
    }
}
