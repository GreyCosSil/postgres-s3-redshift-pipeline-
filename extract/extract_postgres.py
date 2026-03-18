import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os
from pathlib import Path

# caminho absoluto do .env
env_path = Path(__file__).resolve().parent.parent / ".env"

load_dotenv(dotenv_path=env_path)

# agora sim vai funcionar
host = os.getenv("POSTGRES_HOST")
database = os.getenv("POSTGRES_DB")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
port = os.getenv("POSTGRES_PORT")


conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password,
    port=port
)

query = "SELECT * FROM customers"
df = pd.read_sql_query(query, conn)

df.to_csv('data/customers.csv', index=False)
conn.close()
print("Dados Extraidos com sucesso")