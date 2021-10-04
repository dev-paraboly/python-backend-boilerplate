import os
from sqlalchemy import create_engine

user_name = os.getenv('POSTGRE_USER')
password = os.getenv('POSTGRE_PASSWORD')
url = os.getenv('POSTGRE_URL')
port = os.getenv('POSTGRE_PORT', 5432)
dbname = os.getenv('POSTGRE_DBNAME', "transportation")

connection_url = f"postgresql://{user_name}:{password}@{url}:{port}/{dbname}"

sqlalchemy_engine = create_engine(connection_url)
