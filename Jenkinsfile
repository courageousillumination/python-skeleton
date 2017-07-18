
pipeline {
  agent any

  stages {
    stage('Install') {
      steps {
        sh './scripts/ci/install.sh'
      }
    }

    stage('Test') {
      steps {
        sh './scripts/ci/test.sh'
      }

      post {
        always {
          step([$class: 'WarningsPublisher',
          parserConfigurations: [[
            parserName: 'PyLint',
            pattern: 'build/python-lint.txt'
          ]], unstableTotalAll: '0'])

          step([$class: 'CoberturaPublisher',
                autoUpdateHealth: false,
                autoUpdateStability: false,
                coberturaReportFile: 'build/python-coverage.xml',
                failUnhealthy: false,
                failUnstable: false,
                maxNumberOfBuilds: 0,
                onlyStable: false,
                sourceEncoding: 'ASCII',
                zoomCoverageChart: false])
          junit 'build/*-tests.xml'
          junit 'build/python-mypy.xml'
        }
      }
    }
  }
}
