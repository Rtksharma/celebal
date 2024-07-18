import pandas as pd
import pyarrow.parquet as pq
import fastavro
import pyarrow as pa
import sqlite3

# Function to fetch data from the database
def fetch_data(query, db_path):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Save to CSV
def save_to_csv(df, path):
    df.to_csv(path, index=False)

# Save to Parquet
def save_to_parquet(df, path):
    table = pa.Table.from_pandas(df)
    pq.write_table(table, path)

# Save to Avro
def save_to_avro(df, path):
    schema = {
        "type": "record",
        "name": "Record",
        "fields": [{"name": col, "type": "string"} for col in df.columns]
    }
    records = df.to_dict(orient='records')
    with open(path, 'wb') as out:
        fastavro.writer(out, schema, records)

# Example usage
db_path = 'your_database.db'
query = 'SELECT * FROM your_table'

df = fetch_data(query, db_path)
save_to_csv(df, 'data.csv')
save_to_parquet(df, 'data.parquet')
save_to_avro(df, 'data.avro')
import schedule
import time

def job():
    df = fetch_data(query, db_path)
    save_to_csv(df, 'data.csv')
    save_to_parquet(df, 'data.parquet')
    save_to_avro(df, 'data.avro')

# Schedule the job every day at 10:30 AM
schedule.every().day.at("10:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == "path_to_watch":
            job()

observer = Observer()
observer.schedule(FileHandler(), path='path_to_watch', recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
import sqlite3

def copy_all_tables(src_db, dest_db):
    src_conn = sqlite3.connect(src_db)
    dest_conn = sqlite3.connect(dest_db)

    src_cursor = src_conn.cursor()
    src_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = src_cursor.fetchall()

    for table_name in tables:
        table_name = table_name[0]
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", src_conn)
        df.to_sql(table_name, dest_conn, if_exists='replace', index=False)

    src_conn.close()
    dest_conn.close()

# Example usage
src_db = 'source_database.db'
dest_db = 'destination_database.db'
copy_all_tables(src_db, dest_db)
def copy_selected_tables(src_db, dest_db, tables_with_columns):
    src_conn = sqlite3.connect(src_db)
    dest_conn = sqlite3.connect(dest_db)

    for table, columns in tables_with_columns.items():
        query = f"SELECT {', '.join(columns)} FROM {table}"
        df = pd.read_sql_query(query, src_conn)
        df.to_sql(table, dest_conn, if_exists='replace', index=False)

    src_conn.close()
    dest_conn.close()

# Example usage
tables_with_columns = {
    'table1': ['column1', 'column2'],
    'table2': ['column3', 'column4']
}
copy_selected_tables(src_db, dest_db, tables_with_columns)
import pandas as pd
import pyarrow.parquet as pq
import fastavro
import pyarrow as pa
import sqlite3
import schedule
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define all functions as shown above...

# Combined job for the pipeline
def pipeline_job():
    # Copy data to file formats
    df = fetch_data(query, db_path)
    save_to_csv(df, 'data.csv')
    save_to_parquet(df, 'data.parquet')
    save_to_avro(df, 'data.avro')

    # Copy all tables
    copy_all_tables(src_db, dest_db)
    
    # Copy selective tables
    copy_selected_tables(src_db, dest_db, tables_with_columns)

# Scheduling the pipeline
schedule.every().day.at("10:30").do(pipeline_job)

class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == "path_to_watch":
            pipeline_job()

observer = Observer()
observer.schedule(FileHandler(), path='path_to_watch', recursive=False)
observer.start()

try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()



