from datetime import datetime,timedelta,date
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from twitter_etl import run_twitter_etl

default_args={
    'owner': 'airflow',
    'depends_on_past':False,
    'start_date': date(2020,12,1),
    'email':['@gmail.com'],
    'email_on_failure':False,
    'emal_on_retry':False,
    'retries':1,
    'retry_delay':timedelta(minutes=1)
}

dag= DAG(
    'twitter_dag',
    default_args = default_args,
    description='My first etl code'
)

run_etl = PythonOperator(
    task_id='twitter_etl',
    python_callable= run_twitter_etl,
    dag =dag
)
run_etl



