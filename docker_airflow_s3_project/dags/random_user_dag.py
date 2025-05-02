import datetime
from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

from random_user_module import extract_api_data, transform_male_df, load_male_to_s3



default_args = {
  
    'start_date': datetime.datetime(2023, 10, 1),
    'retries': 2,
    'retry_delay': timedelta(seconds=5)
    
}

dag = DAG(
    dag_id='random_user_dag_s3',
    default_args=default_args,
    description='A DAG to send data to S3',
)

#Define the tasks

extract_data = PythonOperator(
        dag=dag,
        python_callable=extract_api_data,
        task_id='get_api_data'
        
    )


extract_male_data = PythonOperator(
        dag=dag,
        python_callable=transform_male_df,
        task_id='get_male_data'
        
    )

write_male_s3data = PythonOperator(
        dag=dag,
        python_callable=load_male_to_s3,
        task_id='write_male_data'
        
    )


extract_data >> extract_male_data >> write_male_s3data
