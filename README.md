# Twitter Data Extraction using Apache Airflow

This project demonstrates how to use Apache Airflow to automate the process of retrieving the last 200 tweets of a specific user from the Twitter API and outputting the data in CSV format.

## Prerequisites

Before running the project, make sure you have the following prerequisites installed:

- Python (>= 3.6)
- Apache Airflow (>= 2.0)
- Tweepy (Python library for accessing the Twitter API)
- Azure Blob Storage account and credentials

## Getting Started

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Tejas-Samel/twitter_pipeline.git
   ```

2. Install the required dependencies using pip:

   ```bash
   pip install tweepy
   ```

3. Configure Twitter API credentials:

   Replace the placeholder values with your actual Twitter API credentials in function ```run_twitter_etl```. You can obtain these credentials by creating a Twitter Developer account and creating an App.

4. Set up Apache Airflow:

   - Make sure you have Apache Airflow installed. You can install it using pip:

     ```bash
     pip install apache-airflow
     ```

   - Initialize the Airflow database:

     ```bash
     airflow db init
     ```

   - Start the Airflow web server and scheduler:

     ```bash
     airflow webserver --port 8080
     airflow scheduler
     ```

5. Create the DAG (Directed Acyclic Graph) for the project:

   - Copy the `twitter_dag.py` file from the repository to your Airflow DAGs folder (usually located at `~/airflow/dags/`).

6. Access the Airflow UI:

   Open a web browser and navigate to `http://localhost:8080`. You should see the Airflow dashboard.

7. Trigger the DAG:

   On the Airflow dashboard, locate the "twitter_dag" DAG and manually trigger it. The DAG will initiate the process of fetching the last 200 tweets of the specified user and exporting the data to a CSV file.

## Directory Structure

```
twitter-airflow-project/
│   config_example.py
│   twitter_dag.py
│   README.md
└───dags/
    │   twitter_dag.py
└───data/
    │   user_tweets.csv
```

## Notes

- The Twitter API has rate limits, so ensure you are aware of these limitations when running the project.
- The CSV output file will be saved in the `data` folder.

Feel free to customize the project as per your requirements and explore more features of Apache Airflow for managing data workflows and automation.

**Disclaimer:** Be cautious about sharing your API credentials and sensitive information. This README assumes you are familiar with basic concepts of Python, Apache Airflow, and Twitter API.
