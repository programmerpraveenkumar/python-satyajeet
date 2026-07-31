from fastapi import FastAPI,Depends
from db_config import get_session
from models import Employee
from sqlmodel import Session, select


app = FastAPI()


@app.get("/")
def sample(session: Session = Depends(get_session)):
    emp_list = session.exec(select(Employee)).all()
    return emp_list

