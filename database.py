from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://sqlserver:sqlserver@p23281621142-u4q1my@gcp-sa-cloud-sql.iam.gserviceaccount.com/AutomatedPublicLibrarySystem?charset=utf8mb4"

engine = create_engine(
  db_connection_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })
with engine.connect() as conn:
    query = text("SELECT * FROM user")
