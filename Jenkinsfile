pipeline {
    agent any

    parameters {
        string(name: 'group_id', defaultValue: 'SALES_L0')
    }

    stages {
        stage('Run') {
            steps {
                echo "Running ETL for ${params.group_id}"
            }
        }
    }
}