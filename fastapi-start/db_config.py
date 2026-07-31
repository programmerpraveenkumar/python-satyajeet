from sqlmodel import SQLModel, create_engine, Session
import os

username="postgres"
password="roottoor"
hostname="localhost"
db_name="ecommerce"


# Replace with your actual database credentials
DATABASE_URL = f"postgresql://{username}:{password}@{hostname}:5432/{db_name}"

engine = create_engine(DATABASE_URL, echo=True)

# def init_db():
#     SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
