
from dotenv import load_dotenv, find_dotenv

import psycopg2

import os


# look for .env path
load_dotenv(find_dotenv())

# retrieve params
params = dict(
    host=os.environ.get("DB_HOST"),
    port=os.environ.get("DB_PORT"),
    dbname=os.environ.get("DB_NAME"),
    user=os.environ.get("DB_USERNAME"),
    password=os.environ.get("DB_PASSWORD"))

# list tables
conn = psycopg2.connect(**params)
cur = conn.cursor()
res = cur.execute("SELECT * FROM pg_catalog.pg_tables")
tables = cur.fetchall()
print(tables)
