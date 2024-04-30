from datetime import datetime
from airflow import DAG
from airflow.operator.bash import BashOperator

with DAG(
dag_id="hello_world",
start_date=datetime(2024, 4, 24)
schedule="@once",
tags=['tutorial']
)as dag:
  # Tasks are represented as operators
  task1 = BashOperator(task_id="task1", bash_commad="echo task1")
  task1 = BashOperator(task_id="task2", bash_commad="echo task2")
  task1 = BashOperator(task_id="task3", bash_commad="echo task3")
  task1 = BashOperator(task_id="task4", bash_commad="echo task4")


 # set dependencies between tasks
 task1 >> task2 >> task3 >> task4
