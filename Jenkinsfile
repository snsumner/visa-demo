node {
  def project = 'snsumner75'
  def appName = 'cicd-demo'
  def feSvcName = "${appName}"
  def release = env.BRANCH_NAME.replaceAll('_','')
  def imageTag = "quay.io/${project}/${appName}-${env.BRANCH_NAME.toLowerCase()}:${env.BUILD_NUMBER}"
  checkout scm

  stage('Printenv') {
     sh("printenv")
  }

  stage ('Login to Quay.io') {
     sh("docker login -u=\"${env.quay_username}\" -p=\"${env.quay_password}\" quay.io")
  }

  stage ('Build image') {
     sh("docker build -t ${imageTag} .")
  }

  stage ('Push image to Quay.io registry') {
     sh("docker push ${imageTag}")
  }

  stage ("Deploy Application") {

     switch (env.BRANCH_NAME) {
        case "dev_1":
            // Roll out to DEV-INT environment
            def namespace = 'dev-int'
            sh("helm upgrade ${release} charts/. --install --namespace ${namespace} --reuse-values --set buildNumber=${env.BUILD_NUMBER},branch=${env.BRANCH_NAME.toLowerCase()},environment=${namespace},replicaCount=1")
        break

        case "rel_1":
            // Roll out to QA environment
            def namespace = 'qa'
            sh("helm upgrade ${release} charts/. --install --namespace ${namespace} --reuse-values --set buildNumber=${env.BUILD_NUMBER},branch=${env.BRANCH_NAME.toLowerCase()},environment=${namespace},replicaCount=4")
        break

        default:
        break
     }
  }
}
