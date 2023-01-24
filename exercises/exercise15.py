import json
from airflow import DAG
from airflow.operators.python import PythonOperator
from dataclasses import dataclass, asdict

# Define default_args dictionary to pass to the DAG
default_args = {
    'owner': 'me',
    'start_date': datetime(2022, 1, 1),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# Create a DAG instance
dag = DAG(
    'my_dag_id',
    default_args=default_args,
    schedule_interval=timedelta(hours=1)
)

# Define a function that reads the json file and outputs it as stringified json
def read_json_file():
    with open("users.json", "r") as f:
        data = json.load(f)
    return json.dumps(data)

# Define a function that reads the stringified json, transforms it into a list of dataclass instances, prints them and returns nothing
def read_stringified_json(**kwargs):
    task_instance = kwargs['ti']
    json_string = task_instance.xcom_pull(task_ids='read_json_file')
    data = json.loads(json_string)
    
    @dataclass
    class User:
        id: str
        name: str
        city: str
        school: str

    users_list = []
    for item in data:
        users_list.append(User(**item))
    for user in users_list:
        print(asdict(user))

# Create an instance of the PythonOperator
read_json_file_task = PythonOperator(
    task_id='read_json_file',
    python_callable=read_json_file,
    dag=dag
)

# Create another instance of the PythonOperator
read_stringified_json_task = PythonOperator(
    task_id='read_stringified_json',
    python_callable=read_stringified_json,
    provide_context=True,
    dag=dag
)

# Set the dependencies between the tasks
read_stringified_json_task.set_upstream(read_json_file_task)
