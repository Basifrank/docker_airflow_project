FROM apache/airflow:2.9.0


WORKDIR /airflow_s3

COPY requirements.txt /airflow_s3

RUN pip install --no-cache-dir -r /airflow_s3/requirements.txt

