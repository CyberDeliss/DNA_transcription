from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data.config import USER, PASSWORD, HOST, PORT, DB_NAME


SQLALCHEMY_DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

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
