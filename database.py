from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']
# print(sqlalchemy.__version__)

engine = create_engine(
  db_connection_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })


def load_bioinks_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from bioinks_test1"))
    bioinks = []
    for row in result.mappings().all():
      # print(row)
      results_as_dict = row # .mappings().all()
      bioinks.append(results_as_dict)
    print(bioinks)
    return bioinks

#with engine.connect() as connection:
#  result = connection.execute(text("select * from #bioinks_test1"))
#  print(result.all())