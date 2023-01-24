from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import json

# Charbel Tabet and Sidi Abdesslam

# Default args for the DAG
default_args = {
    'owner': 'me',
    'start_date': datetime(2022, 12, 1),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Create the DAG
dag = DAG(
    'read_write_dag',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
)

# Reading task
def read_data_from_api():
    api_url = 'https://opensky-network.org/api/states/all'
    response = requests.get(api_url)
    print(response)
    return response.json 

read_data = PythonOperator(
    task_id='read_data',
    python_callable=read_data_from_api,
    dag=dag,
)

# Writing task
def write_data_to_json(**kwargs):
    data = kwargs['ti'].xcom_pull(task_ids='read_data')
    with open('flights.json', 'w') as f:
        json.dump(data, f)

write_data = PythonOperator(
    task_id='write_data',
    python_callable=write_data_to_json,
    provide_context=True,
    dag=dag,
)

# Define the order in which the tasks should run
read_data >> write_data
