from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STR']
# print(sqlalchemy.__version__)

engine = create_engine(
  db_connection_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row))
    return jobs

with engine.connect() as connection:
  result = connection.execute(text("select * from bioinks_test1"))
  print(result.all())