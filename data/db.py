from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# replace it to config:
user = "test"
password = "test"
host = "localhost"
port = "5432"
db_name = "dna_transcription"

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

Base = declarative_base()
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# engine = create_engine("sqlite:///data/my_base.db")
Session = sessionmaker(bind=engine)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
